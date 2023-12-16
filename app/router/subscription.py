from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.model.general import ErrorModel
from app.model.subscription import ReturnSubscription, CreateSubscriptionForm, ReturnCreateSubscription
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
    sql = """
        SELECT * FROM `Subscription` WHERE account_uuid = %s;
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
    subscription_form = subscription_form.model_dump()
    sql = """
        INSERT INTO `Subscription`
        VALUES (%s, %s);
    """
    result = execute_query(sql, (account_uuid, shop_uuid) + tuple(subscription_form.values()))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "msg": "Success",
                "data": get_subscription(account_uuid)
            }
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "msg": "Fail"
            }
        )
    )
