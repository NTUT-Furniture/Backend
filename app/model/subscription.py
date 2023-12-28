from enum import Enum
from typing import List

from pydantic import BaseModel

from app.utils.as_form import as_form

class Subscription(BaseModel):
    uuid: str
    name: str

class SubscriptionList(BaseModel):
    type: str
    subscriptions: List[Subscription]

@as_form
class SubscriptionForm(BaseModel):
    account_uuid: str
    shop_uuid: str

class TargetEnum(str, Enum):
    account_uuid = "account_uuid"
    shop_uuid = "shop_uuid"
