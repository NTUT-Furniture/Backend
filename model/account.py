from pydantic import BaseModel, Field
from typing import Optional

class modelExample(BaseModel):
    id: int
    name: str
    email: str
    password: str

class responseSuccessModel(BaseModel):
    status: str
    message: Optional[str] = None 