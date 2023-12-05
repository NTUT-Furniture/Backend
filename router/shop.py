import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import Account
from model.general import SuccessModel, ErrorModel
from model.shop import (
    ReturnShop, CreateShopForm, ReturnCreateShop, UpdateShopForm,
)
from utils import auth
from utils.db_process import (
    get_all_results, execute_query, dict_to_sql_command, dict_delete_none, if_exists_in_db,
)

router = APIRouter(
    tags=["shop"]
)

async def prepare_response(result, status_code=status.HTTP_200_OK):
    data = {}
    if result:
        data.update({"data": result})
        message = "Success"
    else:
        message = "Fail"

    content = jsonable_encoder({"msg": message, **data})

    return JSONResponse(status_code=status_code, content=content)

@router.get(
    "/", tags=["get"],
    responses={
        200: {
            "model": ReturnShop
        },
        404: {
            "model": ErrorModel
        }
    }
)
async def get_shop(account_uuid: str):
    sql = "SELECT * FROM `Shop` WHERE account_uuid = %s;"
    result = get_all_results(sql, (account_uuid,))

    return await prepare_response(result)

@router.post(
    "/",
    tags=["create"],
    responses={
        200: {
            "model": ReturnCreateShop
        },
        404: {
            "model": ErrorModel
        }
    }
)
async def create_shop(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_form: CreateShopForm = Depends(CreateShopForm.as_form)
):
    if if_exists_in_db("Shop", "account_uuid", account.account_uuid):
        return await prepare_response(
            result=f"The account {account.account_uuid} already owned a shop",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    shop_id = str(uuid.uuid4())
    shop_form = shop_form.model_dump()
    sql = f"INSERT INTO `Shop` VALUES (%s, %s,  %s, %s, %s, DEFAULT);"

    result = execute_query(sql, (shop_id, account.account_uuid) + tuple(shop_form.values()))
    if result:
        return await prepare_response(shop_id)
    return await prepare_response(
        result="Something went wrong even though the query is successful.",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

@router.put(
    "/",
    tags=["update"],
    responses={
        200: {"model": SuccessModel},
        404: {"model": ErrorModel}
    }
)
async def update_shop(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_form: UpdateShopForm = Depends(UpdateShopForm.as_form)
):
    shop_form = dict_delete_none(shop_form.model_dump())

    sql_set_text, sql_set_values = dict_to_sql_command(shop_form)
    sql = f"UPDATE `Shop` SET {sql_set_text} WHERE account_uuid = %s;"
    result = execute_query(sql, (sql_set_values + (account.account_uuid,)))
    if result:
        return await prepare_response(result)
    return await prepare_response(
        result="Something went wrong even though the query is successful.",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
