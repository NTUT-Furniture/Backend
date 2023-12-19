import datetime
from typing import List

from pydantic import BaseModel

from app.utils.as_form import as_form

class Coupon(BaseModel):
    shop_uuid: str
    discount: int
    coupon_code: str
    expire_time: datetime.date
    update_time: datetime.datetime

class CouponList(BaseModel):
    coupons: List[Coupon]

@as_form
class CreateCouponForm(BaseModel):

    discount: int
    coupon_code: str
    expire_time: datetime.date
