import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

import app.utils.auth as auth
from app.model.account import CreateAccountForm, UpdateAccountForm, Account, AccountList
from app.model.auth import Token
from app.model.general import ErrorModel
from app.router.login import login_for_access_token
from app.utils.db_process import execute_query, dict_to_sql_command, dict_delete_none, get_all_results

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

@router.get(
    path="/all", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": AccountList
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorModel
        },
    },
)
async def get_all_accounts(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)]
):
    if account.role == 1:
        sql = """
            SELECT 
                account_uuid,
                name,
                email,
                phone,
                birthday,
                address,
                is_active,
                role,
                update_time
            FROM Account;
        """
        result: dict = get_all_results(sql)
        if result:
            for account in result:
                if account["birthday"]:
                    account["birthday"] = str(account["birthday"])
                if account["update_time"]:
                    account["update_time"] = str(account["update_time"])

            return AccountList(accounts=[Account(**account) for account in result])
        else:
            raise HTTPException(status_code=400, detail="Something went wrong.")
    else:
        raise HTTPException(status_code=401, detail="You are not an admin.")

@router.post(
    "/", tags=["create"], responses={
        status.HTTP_201_CREATED: {
            "model": Token
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorModel
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": ErrorModel
        },
    }
)
async def create_account(
        account_form: CreateAccountForm = Depends(CreateAccountForm.as_form)
):
    try:
        form = account_form.model_dump()
        account_form = account_form.model_dump()
        form["pwd"] = auth.get_password_hash(account_form["pwd"])
        account_id = str(uuid.uuid4())
        sql = """
            INSERT INTO `Account`
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT, DEFAULT
            );
        """
        result = execute_query(sql, ((account_id,) + (tuple(form.values()))))
        if result:
            return await login_for_access_token(
                form_data=OAuth2PasswordRequestForm(username=form["email"], password=account_form["pwd"])
            )
        raise HTTPException(status_code=400, detail=ErrorModel(msg="Create account fail."))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=ErrorModel(msg=str(e)))

@router.put(
    path="/",
    description="Update current logged in account info. "
                "If a admin token is provided, they may update other accounts by providing corresponding uuid.",
    tags=["update"], responses={
        status.HTTP_200_OK: {
            "model": UpdateAccountForm
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorModel
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorModel
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": ErrorModel
        },
    }
)
async def update_account(
        account_form: Annotated[
            UpdateAccountForm,
            Depends(UpdateAccountForm.as_form)],
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        account_uuid: str | None = None
):
    try:
        form = account_form.model_dump()
        form = dict_delete_none(form)
        if 'pwd' in form:
            form['pwd'] = auth.get_password_hash(form['pwd'])
        sql_set_text, sql_set_values = dict_to_sql_command(form)

        sql = f"""
            UPDATE `Account` SET {sql_set_text}
            WHERE account_uuid = %s;
        """
        if account_uuid:
            if account.role == 1:
                result = execute_query(sql, (sql_set_values + (account_uuid,)))
            else:
                raise HTTPException(status_code=401, detail=ErrorModel(msg="You are not an admin."))
        else:
            result = execute_query(sql, (sql_set_values + (account.account_uuid,)))
        if result:
            return account_form
        else:
            raise HTTPException(status_code=500, detail=ErrorModel(msg="Update account fail."))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=ErrorModel(msg=str(e)))
