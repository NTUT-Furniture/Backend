import uuid

from fastapi import Depends, APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import CreateAccountForm, ReturnCreateAccount
from model.general import ErrorModel

from utils.db_process import execute_query

prefix = "/account"
router = APIRouter(
    prefix=prefix,
    tags=["account", "get"],
)
@router.post("/account", tags=["account"], responses={
    status.HTTP_200_OK: {
        "model": ReturnCreateAccount
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel
    }
})
async def create_account(
        account_form: CreateAccountForm = Depends(CreateAccountForm.as_form)
):
    account_form = account_form.model_dump()
    id = uuid.uuid4()
    sql = """
        INSERT INTO `Account`
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT
        );
    """
    result = execute_query(sql, (str(id),) + tuple(account_form.values()))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({
                "msg": "success",
                "data": id
            })
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({
            "msg": "fail"
        })
    )
