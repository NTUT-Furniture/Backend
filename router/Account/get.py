from fastapi import status, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import ReturnAccount
from model.general import ErrorModel
from utils.db_process import get_all_result
prefix = "/account"
router = APIRouter(
    prefix=prefix,
    tags=["account", "get"],
)

@router.get("/account", tags=["account"], responses={
    status.HTTP_200_OK: {
        "model": ReturnAccount
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel
    }
})
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
        result = get_all_result(sql, (account_uuid,))
    else:
        sql += ";"
        result = get_all_result(sql)
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({
                "msg": "success",
                "data": result
            })
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({
            "msg": "fail",
        })
    )
