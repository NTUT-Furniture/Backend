from pydantic import BaseModel
from typing import Optional, List
from model.general import SuccessModel
from utils.as_form import as_form

class GetShopModel(BaseModel):
    shop_uuid: str
    account_uuid: str
    name: str
    description: str
    image_url: str
    update_time: str
class ReturnShopModel(SuccessModel):
    data: List[GetShopModel]

@as_form
class CreateShopForm(BaseModel):
    account_uuid: str
    name: str
    image_url: str
    description: Optional[str]

@as_form
class UpdateShopForm(BaseModel):
    shop_uuid: str
    name: Optional[str]
    image_url: Optional[str]
    description: Optional[str]
