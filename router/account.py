import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import utils.auth as auth
from model.account import ReturnAccount, CreateAccountForm, ReturnCreateAccount, UpdateAccountForm, Account
from model.general import SuccessModel, ErrorModel
from utils.db_process import execute_query, dict_to_sql_command, dict_delete_none

router = APIRouter(
    tags=["account"],
)

@router.get(
    "/", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": ReturnAccount
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    },
    response_model=Account
)
async def get_account(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)]
):
    return account

@router.post(
    "/", tags=["create"], responses={
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
    account_form["pwd"] = auth.get_password_hash(account_form["pwd"])
    account_id = uuid.uuid4()
    sql = """
        INSERT INTO `Account`
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT
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
    # something went wrong, the result shouldn't be None as the query went successfully.
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "msg": "Something went wrong though the query."
            }
        )
    )

@router.put(
    "/", tags=["update"], responses={
        status.HTTP_200_OK: {
            "model": SuccessModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def update_account(
        account_form: Annotated[
            UpdateAccountForm,
            Depends(UpdateAccountForm.as_form)],
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)]
):
    account_form = account_form.model_dump()
    account_form = dict_delete_none(account_form)
    sql_set_text, sql_set_values = dict_to_sql_command(account_form)
    sql = f"""
        UPDATE `Account` SET {sql_set_text} 
        WHERE account_uuid = %s;
    """
    result = execute_query(sql, (sql_set_values + (account.account_uuid,)))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=get_account(account)
        )
    # something went wrong, the result shouldn't be None as the query went successfully.
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "msg": "Something went wrong though the query is successful."
            }
        )
    )
