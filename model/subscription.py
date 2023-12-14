from typing import Optional, List

from pydantic import BaseModel

from model.general import SuccessModel
from utils.as_form import as_form

class Subscription(BaseModel):
    account_uuid: str
    shop_uuid: str

class ReturnSubscription(SuccessModel):
    data: List[Subscription]

@as_form
class CreateSubscriptionForm(BaseModel):
    account_uuid: str
    shop_uuid: str

class ReturnCreateSubscription(SuccessModel):
    data: str
