import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

import app.utils.auth as auth
from app.model.account import CreateAccountForm, UpdateAccountForm, Account
from app.model.general import SuccessModel
from app.utils.db_process import execute_query, dict_to_sql_command, dict_delete_none

router = APIRouter(
    tags=["account"],
)

@router.get(
    "/", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": Account
        },
    },
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
            "model": SuccessModel
        },
    }
)
async def create_account(
        account_form: CreateAccountForm = Depends(CreateAccountForm.as_form)
):
    try:
        account_form = account_form.model_dump()
        account_form["pwd"] = auth.get_password_hash(account_form["pwd"])
        account_id = str(uuid.uuid4())
        sql = """
            INSERT INTO `Account`
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT, DEFAULT
            );
        """
        result = execute_query(sql, ((account_id,) + (tuple(account_form.values()))))
        if result:
            return SuccessModel(data=account_id)
        else:
            raise HTTPException(status_code=400, detail="Something went wrong.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.put(
    "/", tags=["update"], responses={
        status.HTTP_200_OK: {
            "model": SuccessModel
        },
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
    try:
        account_form = account_form.model_dump()
        account_form = dict_delete_none(account_form)
        if 'pwd' in account_form:
            account_form['pwd'] = auth.get_password_hash(account_form['pwd'])
        sql_set_text, sql_set_values = dict_to_sql_command(account_form)
        sql = f"""
            UPDATE `Account` SET {sql_set_text} 
            WHERE account_uuid = %s;
        """
        result = execute_query(sql, (sql_set_values + (account.account_uuid,)))
        if result:
            return SuccessModel(msg="success")
        else:
            raise HTTPException(status_code=400, detail="Something went wrong.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
