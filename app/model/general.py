from pydantic import BaseModel

class SuccessModel(BaseModel):
    msg: str | None = None

class ErrorModel(BaseModel):
    msg: str | None = None
