from pydantic import BaseModel

from model.general import SuccessModel
from utils.as_form import as_form

@as_form
class LoginAccountForm(BaseModel):
    email: str
    pwd: str

class ReturnLoginAccount(SuccessModel):
    data: str
