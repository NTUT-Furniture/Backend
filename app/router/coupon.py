from fastapi import APIRouter, Depends, status, HTTPException

from app.model.coupon import (
    ReturnCoupon, CreateCouponForm, ReturnCreateCoupon, Coupon
)
from app.model.general import SuccessModel, ErrorModel

from app.utils.db_process import get_all_results, execute_query

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
    try:
        sql = """
            SELECT * FROM `Coupon` WHERE shop_uuid = %s;
        """
        result = get_all_results(sql, (shop_uuid,))
        if result:
            coupon = result[0]
            return ReturnCoupon(data=[Coupon(**coupon)])
        else:
            raise HTTPException(status_code=404, detail="Coupon not found.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

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
    try:
        coupon_form = coupon_form.model_dump()
        sql = """
            INSERT INTO `Coupon`
            VALUES (%s, %s, %s, %s, DEFAULT);
        """
        result = execute_query(sql, tuple(coupon_form.values()))
        if result:
            return SuccessModel(data="success")
        else:
            raise HTTPException(status_code=400, detail="Create coupon fail.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
