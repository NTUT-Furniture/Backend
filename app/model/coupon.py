from datetime import datetime, date
from typing import List

from pydantic import BaseModel

from app.utils.as_form import as_form

class Coupon(BaseModel):
    coupon_code: str
    discount: int
    expire_time: date
    update_time: datetime

class CouponList(BaseModel):
    coupons: List[Coupon]

@as_form
class CreateCouponForm(BaseModel):
    coupon_code: str
    discount: int
    expire_time: str

@as_form
class UpdateCouponForm(BaseModel):
    coupon_code: str
    discount: int | None = None
    expire_time: str | None = None
