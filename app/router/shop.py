import uuid
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from app.model.account import Account
from app.model.general import ErrorModel
from app.model.shop import (
    CreateShopForm, UpdateShopForm, Shop, ShopList,
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
            "model": Shop
        },
        status.HTTP_403_FORBIDDEN: {
            "model": ErrorModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_shop(shop_uuid: str):
    sql = "SELECT * FROM `Shop` WHERE shop_uuid = %s AND is_active = 1 LIMIT 1;"
    result = get_all_results(sql, (shop_uuid,))

    if result:
        shop = result[0]
        return Shop(**shop)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Shop with shop_uuid {shop_uuid} not found"
    )

@router.get(
    path="/mine",
    tags=["get"],
    description="Get shop by account_uuid",
    responses={
        status.HTTP_200_OK: {
            "model": Shop
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_shop_by_account(
        account: Annotated[Account, Depends(auth.get_current_active_user)]
):
    sql = "SELECT * FROM `Shop` WHERE account_uuid = %s AND is_active = 1 LIMIT 1;"
    result = get_all_results(sql, (account.account_uuid,))
    if result:
        shop = result[0]
        return Shop(**shop)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Shop with account_uuid {account.account_uuid} not found"
    )

@router.post(
    "/",
    tags=["create"],
    responses={
        status.HTTP_201_CREATED: {
            "model": Shop
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_shop(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_form: CreateShopForm = Depends(CreateShopForm.as_form),
        account_uuid: str | None = None
):
    if account_uuid:
        if account.role == 1:
            account.account_uuid = account_uuid
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )

    if await if_exists_in_db("Shop", "account_uuid", account.account_uuid):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Shop with account_uuid {account.account_uuid} already exists"
        )
    shop_id = str(uuid.uuid4())
    shop_form = shop_form.model_dump()
    sql = f"INSERT INTO `Shop` VALUES (%s, %s,  %s, %s, DEFAULT, DEFAULT);"

    result = execute_query(sql, (shop_id, account.account_uuid) + tuple(shop_form.values()))
    if result:
        return Shop(
            shop_uuid=shop_id,
            account_uuid=account.account_uuid,
            update_time=datetime.now(),
            **shop_form
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Create shop failed."
    )

@router.put(
    "/",
    tags=["update"],
    responses={
        status.HTTP_200_OK: {
            "model": UpdateShopForm
        },
        status.HTTP_403_FORBIDDEN: {
            "model": ErrorModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def update_shop(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_form: UpdateShopForm = Depends(UpdateShopForm.as_form),
        shop_uuid: str | None = None
):
    shop_form = dict_delete_none(shop_form.model_dump())

    sql_set_text, sql_set_values = dict_to_sql_command(shop_form, prefix="S")
    sql = f"UPDATE `Shop` as S SET {sql_set_text} WHERE account_uuid = %s;"
    id = account.account_uuid
    if shop_uuid:
        if account.role == 1:
            sql = f"UPDATE `Shop` as S SET {sql_set_text} WHERE shop_uuid = %s;"
            id = shop_uuid
        else:
            if not await auth.if_account_owns_shop(account.account_uuid, shop_uuid):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Permission denied"
                )
    result = execute_query(sql, (sql_set_values + (id,)))
    if result:
        return UpdateShopForm(**shop_form)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Something went wrong"
    )

@router.get(
    path="/all",
    tags=["get"],
    description="Get all shops. Admins only.",
    responses={
        status.HTTP_200_OK: {
            "model": ShopList
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_all_shops(
        account: Annotated[Account, Depends(auth.get_current_active_user)]
):
    if account.role != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )
    sql = "SELECT * FROM `Shop`;"
    result = get_all_results(sql)
    if result:
        for shop in result:
            shop["update_time"] = str(shop["update_time"])
        return ShopList(shops=[Shop(**shop) for shop in result])
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No shops found"
    )
