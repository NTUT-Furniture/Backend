import datetime
from typing import List

from pydantic import BaseModel

from app.utils.as_form import as_form

class Shop(BaseModel):
    shop_uuid: str
    account_uuid: str
    name: str
    description: str | None = None
    is_active: int | None = None
    update_time: datetime.datetime

class ShopList(BaseModel):
    shops: List[Shop]

@as_form
class CreateShopForm(BaseModel):
    name: str
    description: str | None = None

class CreateShopResponse(CreateShopForm):
    shop_uuid: str
    account_uuid: str

@as_form
class UpdateShopForm(CreateShopForm):
    name: str | None = None
    description: str | None = None
    is_active: int | None = None
