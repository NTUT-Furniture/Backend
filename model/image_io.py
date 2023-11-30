from pydantic import BaseModel, Field
from typing import Optional



class ImageIOSuccessModel(BaseModel):
    filename: str
    content_type: str
    size: int
    success: bool

class ImageIOFailModel(BaseModel):
    status: str
    message: Optional[str] = None
