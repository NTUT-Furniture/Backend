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
    update_time: str

class ProductList(BaseModel):
    products: List[Product]

@as_form
class CreateProductForm(BaseModel):
    name: str
    stock: int
    price: int
    tags: str | None = None
    description: str | None = None
    is_active: int | None = None

@as_form
class UpdateProductForm(CreateProductForm):
    name: str | None = None
    stock: int | None = None
    price: int | None = None
