from enum import Enum

from pydantic import BaseModel

class ImageTypeEnum(str, Enum):
    avatar = "avatar"
    banner = "banner"

class Image(BaseModel):
    image_uuid: str
    content_type: str
    size: int

class ImageIOFailModel(BaseModel):
    msg: str = "Failed"
