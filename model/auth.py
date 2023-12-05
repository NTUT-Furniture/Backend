from pydantic import BaseModel

from utils.as_form import as_form


@as_form
class Auth(BaseModel):
    email: str
    pwd: str


class token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    uuid: str | None = None
