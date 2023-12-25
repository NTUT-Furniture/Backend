import datetime

from pydantic import BaseModel

class TransactionProductLog(BaseModel):
    product_uuid: str
    quantity: int

class TransactionProductLogList(BaseModel):
    transaction_product_logs: list[TransactionProductLog]

class Transaction(BaseModel):
    transaction_uuid: str
    account_uuid: str
    coupon_code: str | None = None
    receive_time: datetime.datetime | None = None
    status: str | None = None
    order_time: datetime.datetime | None = None
    products: TransactionProductLogList

class TransactionCreate(BaseModel):
    account_uuid: str | None = None
    coupon_code: str | None = None
    receive_time: datetime.datetime | None = None
    status: str
    products: TransactionProductLogList

class TransactionList(BaseModel):
    transactions: list[Transaction]
