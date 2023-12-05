from utils import (
    CryptContext,
    OAuth2PasswordBearer,
    jwt,

    datetime, timedelta, pytz,

    Settings, getenv,

    db_process,
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
    encoded_jwt = jwt.encode(to_encode, getenv("secret_key"), algorithm=getenv("algorithm"))
    return encoded_jwt


def authenticate_user(email: str, password: str) -> str | None:
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
            return result[0]["account_uuid"]
    return None
