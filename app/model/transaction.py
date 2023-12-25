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
    coupon_uuid: str | None = None
    receive_time: datetime.datetime
    status: str
    order_time: datetime.datetime
    products: TransactionProductLogList

class TransactionList(BaseModel):
    transactions: list[Transaction]
