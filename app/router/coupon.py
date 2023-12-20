import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from app.model.account import Account
from app.model.coupon import CouponList, CreateCouponForm, Coupon
from app.model.general import ErrorModel
from app.utils import auth
from app.utils.db_process import get_all_results, execute_query, get_shop_by_account_uuid

router = APIRouter(
    tags=["coupon"]
)

@router.get(
    "/", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": CouponList
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_coupons(
        shop_uuid: str
):
    sql = """
        SELECT * FROM `Coupon` WHERE shop_uuid = %s;
    """
    result = get_all_results(sql, (shop_uuid,))
    if result:
        return CouponList(coupons=result)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no coupon for shop_uuid {shop_uuid}"
    )

@router.post(
    "/", tags=["create"], responses={
        status.HTTP_201_CREATED: {
            "model": Coupon
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_coupon(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_uuid: str | None = None,
        coupon_form: CreateCouponForm = Depends(CreateCouponForm.as_form),
):
    if shop_uuid:
        if account.role != 1:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admin can create coupon for other shops."
            )
    else:
        shop_uuid = await get_shop_by_account_uuid(account_uuid=account.account_uuid)
    coupon_form = coupon_form.model_dump()
    sql = """
    SELECT (COUNT(*) > 0) AS exist FROM `Coupon` WHERE shop_uuid = %s AND coupon_code = %s;
    """
    result = get_all_results(sql, (shop_uuid, coupon_form["coupon_code"]))
    if result[0]["exist"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Coupon code {coupon_form['coupon_code']} under shop {shop_uuid} already exists."
        )

    sql = """
        INSERT INTO `Coupon`
        VALUES (%s, %s, %s, %s, DEFAULT);
    """
    result = execute_query(sql, (shop_uuid,) + tuple(coupon_form.values()))
    if result:
        return Coupon(shop_uuid=shop_uuid, update_time=datetime.datetime.now(), **coupon_form)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Create coupon failed."
    )

@router.put(
    "/", tags=["update"], responses={
        status.HTTP_200_OK: {
            "model": Coupon
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def update_coupon(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_uuid: str | None = None,
        coupon_form: CreateCouponForm = Depends(CreateCouponForm.as_form),
):
    if shop_uuid:
        if account.role != 1:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Only admin can update coupon for other shops."
            )
    else:
        shop_uuid = await get_shop_by_account_uuid(account_uuid=account.account_uuid)
    coupon_form = coupon_form.model_dump()
    sql = """
    SELECT (COUNT(*) = 0) AS not_exist FROM `Coupon` WHERE shop_uuid = %s AND coupon_code = %s;
    """
    result = get_all_results(sql, (shop_uuid, coupon_form["coupon_code"]))
    if result[0]["not_exist"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Coupon code {coupon_form['coupon_code']} under shop {shop_uuid} doesn't exist."
        )

    sql = """
        UPDATE `Coupon`
        SET discount = %s, expire_time = %s
        WHERE shop_uuid = %s AND coupon_code = %s;
    """
    result = execute_query(
        sql, (coupon_form["discount"], coupon_form["expire_time"], shop_uuid, coupon_form["coupon_code"])
    )
    if result:
        return Coupon(shop_uuid=shop_uuid, update_time=datetime.datetime.now(), **coupon_form)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Update Coupon failed."
    )
