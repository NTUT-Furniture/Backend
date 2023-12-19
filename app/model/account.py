import datetime

from pydantic import BaseModel, EmailStr

from app.utils.as_form import as_form

class Account(BaseModel):
    account_uuid: str
    name: str
    email: EmailStr
    phone: str | None = None
    birthday: datetime.date | None = None
    address: str | None = None
    is_active: int | None = 1
    role: int | None = 0
    update_time: datetime.datetime | None = None

class AccountList(BaseModel):
    accounts: list[Account]

@as_form
class CreateAccountForm(BaseModel):
    name: str
    email: EmailStr
    pwd: str
    phone: str | None = None
    credit_card: str | None = None
    birthday: datetime.date | None = None
    address: str | None = None

@as_form
class UpdateAccountForm(BaseModel):
    name: str | None = None
    pwd: str | None = None
    phone: str | None = None
    credit_card: str | None = None
    birthday: datetime.date | None = None
    address: str | None = None
    is_active: int | None = None
    role: int | None = None
