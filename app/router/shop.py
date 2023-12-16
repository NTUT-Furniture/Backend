import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse

from app.model.account import Account
from app.model.general import SuccessModel, ErrorModel
from app.model.shop import (
    ReturnShop, CreateShopForm, ReturnCreateShop, UpdateShopForm, Shop,
)
from app.utils import auth
from app.utils.db_process import (
    get_all_results, execute_query, dict_to_sql_command, dict_delete_none, if_exists_in_db,
)

router = APIRouter(
    tags=["shop"]
)

@router.get(
    "/", tags=["get"],
    responses={
        status.HTTP_200_OK: {
            "model": ReturnShop
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_shop(account_uuid: str):
    try:
        sql = "SELECT * FROM `Shop` WHERE account_uuid = %s;"
        result = get_all_results(sql, (account_uuid,))

        if result:
            shop = result[0]
            shop["update_time"] = str(shop["update_time"])
            return ReturnShop(data=[Shop(**shop)])
        raise HTTPException(status_code=404, detail=f"Shop with account_uuid {account_uuid} not found")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.post(
    "/",
    tags=["create"],
    responses={
        status.HTTP_200_OK: {
            "model": ReturnCreateShop
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_shop(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_form: CreateShopForm = Depends(CreateShopForm.as_form)
):
    try:
        if if_exists_in_db("Shop", "account_uuid", account.account_uuid):
            raise HTTPException(status_code=400, detail=f"The account {account.account_uuid} already owned a shop")
        shop_id = str(uuid.uuid4())
        shop_form = shop_form.model_dump()
        sql = f"INSERT INTO `Shop` VALUES (%s, %s,  %s, %s, %s, DEFAULT);"

        result = execute_query(sql, (shop_id, account.account_uuid) + tuple(shop_form.values()))
        if result:
            return SuccessModel(data=shop_id)
        else:
            raise HTTPException(status_code=400, detail="Something went wrong.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.put(
    "/",
    tags=["update"],
    responses={
        status.HTTP_200_OK: {
            "model": SuccessModel
        }
    }
)
async def update_shop(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_form: UpdateShopForm = Depends(UpdateShopForm.as_form)
):
    try:
        shop_form = dict_delete_none(shop_form.model_dump())

        sql_set_text, sql_set_values = dict_to_sql_command(shop_form)
        sql = f"UPDATE `Shop` SET {sql_set_text} WHERE account_uuid = %s;"
        result = execute_query(sql, (sql_set_values + (account.account_uuid,)))
        if result:
            return SuccessModel(msg="success")
        else:
            raise HTTPException(status_code=400, detail="Something went wrong.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
