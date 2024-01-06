import uuid
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from app.model.account import Account
from app.model.coupon import CouponList, CreateCouponForm, UpdateCouponForm, Coupon
from app.model.general import ErrorModel
from app.utils import auth
from app.utils.db_process import get_all_results, execute_query, dict_to_sql_command, dict_delete_none, if_exists_in_db

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
):
    sql = """
        SELECT * FROM `Coupon` WHERE expire_time > now()
    """
    result = get_all_results(sql)
    if result:
        return CouponList(coupons=[Coupon(**coupon) for coupon in result])
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There is no coupon."
    )

@router.get(
    "/all", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": CouponList
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_coupons(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
):
    if account.role != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied."
        )
    sql = """
        SELECT * FROM `Coupon`
    """
    result = get_all_results(sql)
    if result:
        return CouponList(coupons=[Coupon(**coupon) for coupon in result])
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There is no coupon."
    )

@router.post(
    "/", tags=["create"], responses={
        status.HTTP_201_CREATED: {
            "model": CreateCouponForm
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_coupon(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        coupon_form: CreateCouponForm = Depends(CreateCouponForm.as_form),
):
    """
    usage example:
    email@gmail.com
    123

    "coupon_code": "NEWCODE",
    "discount": 10,
    "expire_time": "2024-12-31"
    """
    if account.role != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin can create coupon."
        )
    coupon_form = coupon_form.model_dump()
    coupon_uuid = str(uuid.uuid4())
    sql = """
        INSERT INTO `Coupon`
        VALUES (%s, %s, %s, %s, DEFAULT);
    """
    result = execute_query(
        sql, (
            coupon_uuid, coupon_form["coupon_code"], coupon_form["discount"], coupon_form["expire_time"])
    )
    if result:
        return Coupon(
            coupon_uuid=coupon_uuid,
            update_time=datetime.now(),
            **coupon_form
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Create coupon failed."
    )

@router.put(
    "/", tags=["update"], responses={
        status.HTTP_200_OK: {
            "model": UpdateCouponForm
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def update_coupon(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        coupon_form: UpdateCouponForm = Depends(UpdateCouponForm.as_form),
):
    """
        usage example:
        email@gmail.com
        123

        "coupon_code": "30OFFSHOP",
        "discount": 20,
        "expire_time": "2077-12-31"

        "coupon_code": "30OFFSHOP",
        "expire_time": "2077-12-31"

        "coupon_code": "30OFFSHOP",
        "discount": 20
        """
    if account.role != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can update coupons."
        )
    coupon_form = coupon_form.model_dump()
    coupon_form = dict_delete_none(coupon_form)

    if not await if_exists_in_db(table_name="Coupon", column_name="coupon_uuid", value=coupon_form["coupon_uuid"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad coupon_uuid."
        )

    sql_set_text, sql_set_value = dict_to_sql_command(coupon_form, exclude_col=["coupon_code"], prefix='C')
    sql = f"""
        UPDATE `Coupon` as C 
        set {sql_set_text}
        WHERE coupon_uuid = %s;
    """
    result = execute_query(
        sql, (sql_set_value + (coupon_form["coupon_uuid"],))
    )
    if result:
        return UpdateCouponForm(**coupon_form)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Update Coupon failed."
    )
