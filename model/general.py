from typing import Optional

from pydantic import BaseModel

class SuccessModel(BaseModel):
    status: str
    msg: Optional[str] = None

class ErrorModel(BaseModel):
    status: str
    msg: Optional[str] = None
