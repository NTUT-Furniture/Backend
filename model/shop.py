from pydantic import BaseModel

from typing import Optional, List

from model.general import SuccessModel

from utils.as_form import as_form

class Shop(BaseModel):
    shop_uuid: str
    account_uuid: str
    name: str
    description: str
    image_url: str
    update_time: str

class ReturnShop(SuccessModel):
    data: List[Shop]

@as_form
class CreateShopForm(BaseModel):
    account_uuid: str
    name: str
    image_url: str
    description: Optional[str]

class ReturnCreateShop(SuccessModel):
    data: str

@as_form
class UpdateShopForm(BaseModel):
    shop_uuid: str
    name: Optional[str]
    image_url: Optional[str]
    description: Optional[str]
