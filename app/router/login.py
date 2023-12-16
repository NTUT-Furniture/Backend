from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.model.auth import *
from app.utils.auth import *

router = APIRouter(
    tags=["account"]
)

@router.post(
    "/token",
    response_model=Token,
)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    # the username here is actually the email.
    # Due to some bullshit reasons, the scope functionality to be precisely, gotta use this model.,
    token_data: TokenData = authenticate_user(form_data.username, form_data.password)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Settings["access_token_expire_minutes"])
    access_token = create_access_token(
        data={"sub": token_data.uuid}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
