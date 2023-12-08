from datetime import datetime, timedelta
from os import getenv
from typing import Annotated

import pytz
from fastapi import Depends, HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from core.settings import Settings
from model.account import Account
from model.auth import TokenData
from utils import db_process

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    utc_time = datetime.now(pytz.timezone('UTC'))
    utc_plus_8 = utc_time.astimezone(pytz.timezone('Asia/Taipei'))
    if expires_delta:
        expire = utc_plus_8 + expires_delta
    else:
        expire = utc_plus_8 + timedelta(minutes=Settings["access_token_expire_minutes"])
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM"))
    return encoded_jwt

def authenticate_user(email: str, password: str) -> TokenData | None:
    script = """
        SELECT 
            email,
            account_uuid,
            pwd
        From Account
        WHERE email = %s;
    """
    result = db_process.get_all_results(script, (email,))
    if result:
        if verify_password(password, result[0]["pwd"]):
            return TokenData(uuid=result[0]["account_uuid"])
    return None

def get_account(uuid: str) -> Account | None:
    script = """
        SELECT
            account_uuid,
            name,
            email,
            phone,
            birthday,
            address,
            is_active,
            update_time
        FROM Account
        WHERE account_uuid = %s;            
   """

    result = db_process.get_all_results(script, (uuid,))
    if result:
        account = result[0]
        account["birthday"] = account["birthday"].strftime("%Y-%m-%d")
        account["update_time"] = account["update_time"].strftime("%Y-%m-%d %H:%M:%S")
        return Account(**account)
    return None

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> Account:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")])
        user_uuid: str = payload.get("sub")
        if user_uuid is None:
            raise credentials_exception
        token_data = TokenData(uuid=user_uuid)
    except JWTError:
        raise credentials_exception
    user = get_account(uuid=token_data.uuid)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
        current_user: Annotated[Account, Depends(get_current_user)]
):

    # TODO: Add disabled column to Account table
    # if current_user.disabled:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="Inactive user"
    #     )
    return current_user

async def if_account_owns_shop(
        account_uuid: str,
        shop_uuid: str
) -> bool:
    return await db_process.if_one_owns_the_other(
        "Shop", "account_uuid", account_uuid
        , "shop_uuid", shop_uuid
    )

async def if_shop_owns_product(
        shop_uuid: str,
        product_uuid: str
) -> bool:
    return await db_process.if_one_owns_the_other(
        "Product", "shop_uuid",
        shop_uuid, "product_uuid", product_uuid
    )

async def if_account_owns_product(
        account_uuid: str,
        shop_uuid: str,
        product_uuid: str
) -> bool:
    return await if_account_owns_shop(account_uuid, shop_uuid) and \
        await if_shop_owns_product(shop_uuid, product_uuid)
