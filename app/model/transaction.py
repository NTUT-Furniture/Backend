import datetime
from enum import Enum

from pydantic import BaseModel

class TransactionTargetEnum(str, Enum):
    Account = "Account"
    Shop = "Shop"

class TransactionStatusEnum(str, Enum):
    Ordered = "Ordered"
    Delivering = "Delivering"
    Arrived = "Arrived"
    Cancelled = "Cancelled"

class TransactionProductLog(BaseModel):
    product_name: str | None = None
    product_uuid: str
    product_description: str | None = None
    quantity: int
    price: int | None = None

class TransactionProductLogList(BaseModel):
    transaction_product_logs: list[TransactionProductLog]

class Transaction(BaseModel):
    transaction_uuid: str
    account_uuid: str
    shop_uuid: str
    discount: float | None = None
    receive_time: datetime.datetime | None = None
    status: TransactionStatusEnum
    order_time: datetime.datetime | None = None
    products: TransactionProductLogList
    total_price: float | None = None

class TransactionCreate(BaseModel):
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
