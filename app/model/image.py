from enum import Enum

from pydantic import BaseModel

from app.model.general import SuccessModel

class ImageTypeModel(str, Enum):
    avatar = "avatar"
    banner = "banner"

class ImageUploadSuccessModel(SuccessModel):
    image_uuid: str
    content_type: str
    size: int

class ImageIOFailModel(BaseModel):
    msg: str = "Failed"
