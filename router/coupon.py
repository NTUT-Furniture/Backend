from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.coupon import ReturnCoupon, CreateCouponForm, ReturnCreateCoupon, UpdateCouponForm
from model.general import SuccessModel, ErrorModel

from utils.db_process import get_all_results, execute_query, dict_to_sql_command, dict_delete_none

router = APIRouter(
    tags=["coupon"]
)

@router.get(
    "/", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": ReturnCoupon
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_coupon(
    shop_uuid: str
):
    sql = """
        SELECT * FROM `Coupon` WHERE shop_uuid = %s;
    """
    result = get_all_results(sql, (shop_uuid,))
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
            "model": ReturnCreateCoupon
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_coupon(
    coupon_form: CreateCouponForm = Depends(CreateCouponForm.as_form)
):
    coupon_form = coupon_form.model_dump()
    sql = """
        INSERT INTO `Coupon`
        VALUES (%s, %s, %s, %s, DEFAULT);
    """
    result = execute_query(sql, tuple(coupon_form.values()))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "msg": "Success",
                    "data": "Hi"
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
async def update_coupon(
    coupon_form: UpdateCouponForm = Depends(UpdateCouponForm.as_form)
):
    coupon_form = coupon_form.model_dump()
    coupon_form = dict_delete_none(coupon_form)
    sql_set_text, sql_set_values = dict_to_sql_command(coupon_form)
    sql = f"""
        UPDATE `Coupon` SET {sql_set_text}
        WHERE shop_uuid = %s;
    """
    result = execute_query(sql, (sql_set_values + (coupon_form["shop_uuid"],)))
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
