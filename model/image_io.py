from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel

from model.general import SuccessModel
from utils.as_form import as_form

@as_form
class ImageIOSuccessModel(SuccessModel):
    file_name: str
    content_type: str
    size: int
    file: Optional[UploadFile] = None

class ImageIOFailModel(BaseModel):
    msg: str = ""
