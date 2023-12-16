from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.model.general import SuccessModel, ErrorModel
from app.model.subscription import (
    ReturnSubscription, CreateSubscriptionForm, ReturnCreateSubscription, Subscription
)
from app.utils.db_process import get_all_results, execute_query

router = APIRouter(
    tags=["subscription"]
)

@router.get(
    "/", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": ReturnSubscription
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_subscription(
        account_uuid: str
):
    try:
        sql = """
            SELECT * FROM `Subscription` WHERE account_uuid = %s;
        """
        result = get_all_results(sql, (account_uuid,))
        if result:
            subscription = result[0]
            return ReturnSubscription(data=[Subscription(**subscription)])
        else:
            raise HTTPException(status_code=400, detail="Get subscription fail.")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post(
    "/", tags=["create"], responses={
        status.HTTP_200_OK: {
            "model": ReturnCreateSubscription
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_subscription(
        account_uuid: str,
        shop_uuid: str,
        subscription_form: CreateSubscriptionForm = Depends(CreateSubscriptionForm.as_form)
):
    try:
        subscription_form = subscription_form.model_dump()
        sql = """
            INSERT INTO `Subscription`
            VALUES (%s, %s);
        """
        result = execute_query(sql, (account_uuid, shop_uuid) + tuple(subscription_form.values()))
        if result:
            return SuccessModel(data=(account_uuid, shop_uuid))
        else:
            raise HTTPException(status_code=400, detail="Create subscription fail.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
