import uuid

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.shop import ReturnShop, CreateShopForm, ReturnCreateShop, UpdateShopForm
from model.general import SuccessModel, ErrorModel

from utils.db_process import get_all_results, execute_query, dict_to_sql_command, dict_delete_none

router = APIRouter(
    tags=["shop"]
)

@router.get(
    "/", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": ReturnShop
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_shop(
    account_uuid: str
):
    sql = """
        SELECT * FROM `Shop` WHERE account_uuid = %s;
    """
    result = get_all_results(sql, (account_uuid,))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "msg": "Success",
                    "data": result
                }
            )
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "msg": "Fail"
            }
        )
    )

@router.post(
    "/", tags=["create"], responses={
        status.HTTP_200_OK: {
            "model": ReturnCreateShop
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_shop(
    shop_form: CreateShopForm = Depends(CreateShopForm.as_form)
):
    shop_form = shop_form.model_dump()
    shop_id = uuid.uuid4()
    sql = """
        INSERT INTO `Shop`
        VALUES (%s, %s, %s, %s, %s, DEFAULT);
    """
    result = execute_query(sql, (str(shop_id),) + tuple(shop_form.values()))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "msg": "Success",
                    "data": shop_id
                }
            )
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "msg": "Fail"
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
async def update_shop(
    shop_form: UpdateShopForm = Depends(UpdateShopForm.as_form)
):
    shop_form = shop_form.model_dump()
    shop_form = dict_delete_none(shop_form)
    sql_set_text, sql_set_values = dict_to_sql_command(shop_form)
    sql = f"""
        UPDATE `Shop` SET {sql_set_text}
        WHERE shop_uuid = %s;
    """
    result = execute_query(sql, (sql_set_values + (shop_form["shop_uuid"],)))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "msg": "Success"
                }
            )
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "msg": "Fail"
            }
        )
    )
