from pydantic import BaseModel, Field
from typing import Optional
from utils.as_form import as_form

class SuccessModel(BaseModel):
    status: str
    msg: Optional[str] = None

class ErrorModel(BaseModel):
    status: str
    msg: Optional[str] = None