from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from model.auth import *
from utils.auth import *

router = APIRouter(
    tags=["account"]
)

@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    # the username here is actually the email.
    # Due to some bullshit reasons, the scope functionality to be precisely, gotta use this model.,
    user_uuid = authenticate_user(form_data.username, form_data.password)
    if not user_uuid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Settings["access_token_expire_minutes"])
    access_token = create_access_token(
        data={"sub": user_uuid}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
