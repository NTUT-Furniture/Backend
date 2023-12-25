import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.model.account import Account
from app.model.general import ErrorModel
from app.model.transaction import TransactionList, Transaction, TransactionCreate
from app.utils.auth import get_current_active_user
from app.utils.db_process import get_all_results, execute_query

router = APIRouter(
    tags=["account", "transaction", "product", "coupon", "shop"]
)

@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {
            "model": TransactionList
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorModel
        },
        status.HTTP_403_FORBIDDEN: {
            "model": ErrorModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_transaction_list(
        account: Annotated[
            Account,
            Depends(get_current_active_user)],
        account_uuid: str | None = None
):
    """
    Get transaction list of current logged in account.
    :param account:  Current logged in account
    :param account_uuid: Admins may provide an account_uuid to get transaction list of that account.
    :return: TransactionList
    :raises HTTPException 401: Unauthorized, HTTPException 403: Forbidden,    HTTPException 404: Not found
    """
    sql = "SELECT * FROM Transaction WHERE account_uuid = %s"

    if account.role == 1 and account_uuid:
        result = get_all_results(sql, (account_uuid,))
    else:
        result = get_all_results(sql, (account.account_uuid,))

    if result:
        for transaction in result:
            transaction["products"] = get_all_results(
                "SELECT * FROM TransactionProductLog WHERE transaction_uuid = %s",
                (transaction["transaction_uuid"],)
            )
        return {"transactions": result}

@router.post(
    path="/",
    responses={
        status.HTTP_201_CREATED: {
            "model": Transaction
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorModel
        },
        status.HTTP_403_FORBIDDEN: {
            "model": ErrorModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_transaction(
        account: Annotated[
            Account,
            Depends(get_current_active_user)],
        transaction: TransactionCreate,
):
    """
    Create a transaction. Admins may provide an account_uuid to create a transaction for that account.
    :param account: Current logged in account
    :param transaction: TransactionCreate
    :return: Transaction

    :raises HTTPException 401: Unauthorized, HTTPException 403: Forbidden,    HTTPException 404: Not found
    """

    transaction_uuid = str(uuid.uuid4())
    account_uuid = transaction.account_uuid if transaction.account_uuid and account.role == 1 else account.account_uuid
    sql = """
    INSERT INTO 
    Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) 
    VALUES (%s, %s, %s, %s, %s, DEFAULT)
    """
    values = (
        transaction_uuid,
        account_uuid,
        transaction.coupon_code,
        transaction.receive_time,
        transaction.status
    )

    result: bool = execute_query(sql, values)
    if result:
        for product in transaction.products.transaction_product_logs:
            sql = """
            INSERT INTO 
            TransactionProductLog (transaction_uuid, product_uuid, quantity) 
            VALUES (%s, %s, %s)
            """
            values = (
                transaction_uuid,
                product.product_uuid,
                product.quantity
            )
            execute_query(sql, values)

        return Transaction(
            transaction_uuid=transaction_uuid,
            account_uuid=account_uuid,
            coupon_code=transaction.coupon_code,
            receive_time=transaction.receive_time,
            status=transaction.status,
            products=transaction.products
        )
