from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import UpdateAccountForm, CreateAccount
from model.general import SuccessModel
from utils.db_process import get_all_result, execute_query, dict_to_sql_command, dict_delete_none

router = APIRouter()

@router.get("/account", tags=["account"], responses={
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
            "msg": "success",
            "data": result
        })
    )
@router.post("/account", tags=["account"], responses={
    status.HTTP_200_OK: {
        "model": SuccessModel
    },
})
async def create_account(
    account_form: CreateAccount = Depends(CreateAccount.as_form)
):
    account_form = account_form.model_dump()
    print(account_form)
    sql = f"""
        INSERT INTO `Account`
        VALUES(
            UUID(), %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT
        );
    """
    result = execute_query(sql, tuple(account_form.values()))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({
                "msg": "success"
            })
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({
                "msg": "fail"
            })
        )
@router.put("/account", tags=["account"], responses={
    status.HTTP_200_OK: {
        "model": SuccessModel
    },
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
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "success"
        })
    )
