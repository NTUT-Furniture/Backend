from typing import Optional

from pydantic import BaseModel

from app.utils.as_form import as_form

class Account(BaseModel):
    account_uuid: str
    name: str
    email: str
    phone: Optional[str]
    birthday: Optional[str]
    address: Optional[str]
    is_active: int
    role: int
    update_time: str

@as_form
class CreateAccountForm(BaseModel):
    name: str
    email: str
    pwd: str
    phone: Optional[str] = None
    credit_card: Optional[str] = None
    birthday: Optional[str] = None
    address: Optional[str] = None

@as_form
class UpdateAccountForm(BaseModel):
    name: Optional[str]
    email: Optional[str]
    pwd: Optional[str]
    phone: Optional[str]
    credit_card: Optional[str]
    birthday: Optional[str]
    address: Optional[str]
    is_active: Optional[bool]
