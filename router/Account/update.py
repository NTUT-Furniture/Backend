from fastapi import Depends
from fastapi import status, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import UpdateAccountForm
from model.general import ErrorModel, SuccessModel

from utils.db_process import execute_query, dict_delete_none, dict_to_sql_command

prefix = "/account"
router = APIRouter(
    prefix=prefix,
    tags=["account", "get"],
)
@router.put("/account", tags=["account"], responses={
    status.HTTP_200_OK: {
        "model": SuccessModel
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel
    }
})
async def update_account(
        account_form: UpdateAccountForm = Depends(UpdateAccountForm.as_form)
):
    account_form = account_form.model_dump()
    account_form = dict_delete_none(account_form)
    sql_set_text, sql_set_values = dict_to_sql_command(account_form)
    sql = f"""
        UPDATE `Account` SET {sql_set_text} WHERE account_uuid = %s;
    """
    result = execute_query(sql, (sql_set_values + (account_form["account_uuid"],)))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({
                "msg": "success"
            })
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({
            "msg": "fail"
        })
    )
