from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Request
from model.general import SuccessModel, ErrorModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from utils.db_process import get_all_result, execute_query, dict_to_sqltext, dict_delete_none
from model.account import UpdateAccountForm

router = APIRouter()

@router.get("/account", tags=["example"], responses={
    status.HTTP_200_OK: {
        "model": SuccessModel
    },
})
async def get_account():
    sql = """
        SELECT account_uuid, name, pwd, update_time FROM `Account`;
    """
    result = get_all_result(sql)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
                "data":result
            })
)

@router.put("/account", tags=["example"], responses={
    status.HTTP_200_OK: {
        "model": SuccessModel
    },
})
async def update_account(
    account_form: UpdateAccountForm = Depends(UpdateAccountForm.as_form)
):
    account_form = account_form.model_dump()
    account_form = dict_delete_none(account_form)

    sql_set_text, sql_set_values = dict_to_sqltext(account_form)
    sql = f"""
        UPDATE `Account` SET {sql_set_text} WHERE account_uuid = %s;
    """
    result = execute_query(sql,(sql_set_values+(account_form["account_uuid"],)))
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
                "data":result
            })
    )

