from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    uuid: str | None = None
    role: str = "user"  # value: user, admin
