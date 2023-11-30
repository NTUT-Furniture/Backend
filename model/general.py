from pydantic import BaseModel

class SuccessModel(BaseModel):
    msg: str = "Success"

class ErrorModel(BaseModel):
    msg: str = "Fail"
