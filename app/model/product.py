from typing import Optional, List

from pydantic import BaseModel

from app.model.general import SuccessModel
from app.utils.as_form import as_form

class Product(BaseModel):
    product_uuid: str
    shop_uuid: str
    name: str
    stock: int
    image_url: str
    price: int
    tags: str
    description: str
    update_time: str

class ReturnProduct(SuccessModel):
    data: List[Product]

@as_form
class CreateProductForm(BaseModel):
    shop_uuid: str
    name: str
    stock: int
    image_url: str
    price: int
    tags: Optional[str] = None
    description: Optional[str] = None

class ReturnCreateProduct(SuccessModel):
    data: str

@as_form
class UpdateProductForm(BaseModel):
    product_uuid: str
    shop_uuid: str
    name: Optional[str]
    stock: Optional[int]
    image_url: Optional[str]
    price: Optional[int]
    tags: Optional[str]
    description: Optional[str]
