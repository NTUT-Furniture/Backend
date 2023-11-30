import uuid

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import CreateAccountForm, ReturnCreateAccount, UpdateAccountForm, ReturnAccount
from model.general import ErrorModel, SuccessModel
from utils.db_process import get_all_results, execute_query, dict_delete_none, dict_to_sql_command

router = APIRouter(
    tags=["account"],
)

@router.post(
    "/", tags=["create", "HTTP_POST"], responses={
        status.HTTP_200_OK: {
            "model": ReturnCreateAccount
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_account(
        account_form: CreateAccountForm = Depends(CreateAccountForm.as_form)
):
    account_form = account_form.model_dump()
    account_id = uuid.uuid4()
    sql = """
        INSERT INTO `Account`
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT
        );
    """
    result = execute_query(sql, (str(account_id),) + tuple(account_form.values()))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "msg": "success",
                    "data": account_id
                }
            )
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "msg": "fail"
            }
        )
    )

@router.put(
    "/", tags=["update", "HTTP_PUT"], responses={
        status.HTTP_200_OK: {
            "model": SuccessModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def update_account(
        account_form: UpdateAccountForm = Depends(UpdateAccountForm.as_form)
):
    account_form = account_form.model_dump()
    account_form = dict_delete_none(account_form)
    sql_set_text, sql_set_values = dict_to_sql_command(account_form)
    sql = f"""UPDATE `Account` SET {sql_set_text} WHERE account_uuid = %s;"""
    result = execute_query(sql, (sql_set_values + (account_form["account_uuid"],)))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "msg": "success"
                }
            )
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "msg": "fail"
            }
        )
    )

@router.get(
    "/", tags=["get", "HTTP_GET"], responses={
        status.HTTP_200_OK: {
            "model": ReturnAccount
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_account(
        account_uuid: str = None
):
    sql = """
        SELECT
            account_uuid,
            name,
            image_url,
            email,
            phone,
            birthday,
            address,
            is_active,
            update_time
        FROM `Account`
    """
    if account_uuid is not None:
        sql += " WHERE account_uuid = %s;"
        result = get_all_results(sql, (account_uuid,))
    else:
        sql += ";"
        result = get_all_results(sql)
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "msg": "success",
                    "data": result
                }
            )
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "msg": "fail"
            }
        )
    )
