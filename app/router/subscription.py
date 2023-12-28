from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

import app.utils.auth as auth
from app.model.account import Account
from app.model.general import ErrorModel
from app.model.subscription import Subscription, SubscriptionList, TargetEnum
from app.utils.db_process import get_all_results, get_shop_by_account_uuid, execute_query

router = APIRouter(
    tags=["subscription", "account", "shop"],
)

@router.get(
    "/account", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": SubscriptionList
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        },
    },
)
async def get_subscription(
        uuid_type: TargetEnum,
        uuid: str | None = None,
):
    table = "Shop" if uuid_type == TargetEnum.account_uuid else "Account"
    target = TargetEnum.shop_uuid if uuid_type == TargetEnum.account_uuid else TargetEnum.account_uuid
    script = f"""
        SELECT 
            S.{target.value} AS uuid,
            T.name
        FROM Subscription AS S
        LEFT JOIN {table} AS T ON S.{target.value} = T.{target.value}
        WHERE S.{uuid_type.value} = %s
    """
    result = get_all_results(script, (uuid,))
    if result:
        return SubscriptionList(type=target.value, subscriptions=[Subscription(**subscription) for subscription in result])
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Subscription not found."
    )

@router.post(
    path="/",
    description="Subscribe to a shop.\n Admins may make others subscribe a shop by providing an account_uuid.",
    tags=["post"],
    responses={
        status.HTTP_201_CREATED: {
            "model": Subscription
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorModel
        },
    },
)
async def subscribe(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        shop_uuid: str,
        account_uuid: str | None = None
):
    if not (account.role == 1 and account_uuid):
        account_uuid = account.account_uuid

    script = """
        INSERT INTO Subscription (account_uuid, shop_uuid)
        VALUES (%s, %s);
    """
    try:
        result = execute_query(script, (account_uuid, shop_uuid))
    except HTTPException as e:
        if "Duplicate entry" in e.detail:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Account {account_uuid} has already subscribed shop {shop_uuid}."
            )
        raise e
    if result:
        return Subscription(account_uuid=account_uuid, shop_uuid=shop_uuid)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Failed to subscribe."
    )

@router.delete(
    "/unsubscribe", tags=["delete"], responses={
        status.HTTP_200_OK: {
            "model": Subscription
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorModel
        },
    },
)
async def unsubscribe(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        shop_uuid: str,
        account_uuid: str | None = None
):
    if not (account.role == 1 and account_uuid):
        account_uuid = account.account_uuid
    script = """
        DELETE FROM Subscription
        WHERE account_uuid = %s AND shop_uuid = %s;
    """
    result = execute_query(script, (account_uuid, shop_uuid))
    if result:
        return Subscription(account_uuid=account_uuid, shop_uuid=shop_uuid)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Failed to unsubscribe."
    )
