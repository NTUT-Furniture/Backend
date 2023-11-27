from typing import Optional

from pydantic import BaseModel

from utils.as_form import as_form

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

@as_form
class CreateAccount(BaseModel):
    name: str
    pwd: str
    image_url: str
    email: Optional[str] = None
    phone: Optional[str] = None
    credit_card: Optional[str] = None
    birthday: Optional[str] = None
    address: Optional[str] = None
