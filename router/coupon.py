from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.coupon import ReturnCoupon, CreateCouponForm, ReturnCreateCoupon
from model.general import ErrorModel

from utils.db_process import get_all_results, execute_query

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
                    "data": ""
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
