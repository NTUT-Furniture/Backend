import datetime
from enum import Enum

from pydantic import BaseModel

class TransactionStatusEnum(str, Enum):
    Ordered = "Ordered"
    Delivering = "Delivering"
    Arrived = "Arrived"
    Cancelled = "Cancelled"

class TransactionProductLog(BaseModel):
    product_uuid: str
    quantity: int

class TransactionProductLogList(BaseModel):
    transaction_product_logs: list[TransactionProductLog]

class Transaction(BaseModel):
    transaction_uuid: str
    account_uuid: str
    shop_uuid: str
    coupon_code: str | None = None
    receive_time: datetime.datetime | None = None
    status: TransactionStatusEnum
    order_time: datetime.datetime | None = None
    products: TransactionProductLogList

class TransactionCreate(BaseModel):
    account_uuid: str | None = None
    shop_uuid: str
    coupon_code: str | None = None
    receive_time: datetime.datetime | None = None
    status: TransactionStatusEnum
    products: TransactionProductLogList

class TransactionUpdate(BaseModel):
    receive_time: datetime.datetime | None = None
    status: TransactionStatusEnum | None = None

class TransactionList(BaseModel):
    transactions: list[Transaction]
