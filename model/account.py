from pydantic import BaseModel, Field
from typing import Optional

class modelExample(BaseModel):
    id: int
    name: str
    email: str
    password: strfrom typing import Optional, List

from pydantic import BaseModel

from utils.as_form import as_form

from model.general import SuccessModel

class Account(BaseModel):
    account_uuid: str
    name: str
    image_url: str
    email: str
    phone: str
    birthday: str
    address: str
    is_active: int
    update_time: str

class ReturnAccount(SuccessModel):
    data: List[Account]

@as_form
class CreateAccountForm(BaseModel):
    name: str
    pwd: str
    image_url: str
    email: Optional[str] = None
    phone: Optional[str] = None
    credit_card: Optional[str] = None
    birthday: Optional[str] = None
    address: Optional[str] = None

class ReturnCreateAccount(SuccessModel):
    data: str

@as_form
class UpdateAccountForm(BaseModel):
    account_uuid: str
    name: Optional[str]
    pwd: Optional[str]
    image_url: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    credit_card: Optional[str]
    birthday: Optional[str]
    address: Optional[str]
    is_active: Optional[bool]
