import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel

from app.utils.as_form import as_form

class Product(BaseModel):
    product_uuid: str
    shop_uuid: str
    name: str
    stock: int
    price: int
    tags: str | None = None
    description: str | None = None
    is_active: int | None = None
    update_time: datetime.datetime

class ProductList(BaseModel):
    products: List[Product]

@as_form
class CreateProductForm(BaseModel):
    name: str
    stock: int
    price: int
    tags: str | None = None
    description: str | None = None
    is_active: int | None = 1

class CreateProductResponse(BaseModel):
    product_uuid: str
    shop_uuid: str
    name: str
    stock: int
    price: int
    tags: str | None = None
    description: str | None = None
    is_active: int | None = None

@as_form
class UpdateProductForm(BaseModel):
    product_uuid: str
    name: str | None = None
    stock: int | None = None
    price: int | None = None
    tags: str | None = None
    description: str | None = None
    is_active: int | None = None

class OrderEnum(str, Enum):
    product_uuid = "product_uuid"
    shop_uuid = "shop_uuid"
    name = "name"
    stock = "stock"
    price = "price"
    tags = "tags"
    description = "description"
    is_active = "is_active"
    update_time = "update_time"
    random = "RAND()"

@as_form
class GetProductForm(BaseModel):
    shop_uuid: str | None = None
    is_active: int | None = 1
    from_price: int | None = 0
    to_price: int | None = 4294967295
    from_stock: int | None = 0
    to_stock: int | None = 4294967295
    tags: str | None = None
    start: int | None = 0
    limit: int | None = 10
