from pydantic import BaseModel
from typing import Optional, Union
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

