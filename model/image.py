from fastapi import UploadFile
from pydantic import BaseModel

from model.general import SuccessModel
from utils.as_form import as_form

@as_form
class ImageUploadForm(BaseModel):
    owner_uuid: str
    file: UploadFile

class ImageUploadSuccessModel(SuccessModel):
    image_uuid: str
    content_type: str
    size: int

@as_form
class ImageGetForm(BaseModel):
    owner_uuid: str
    file_uuid: str

class ImageIOFailModel(BaseModel):
    msg: str = ""
