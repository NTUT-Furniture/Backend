import uuid
from typing import Annotated, Dict

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.model.account import Account
from app.model.general import ErrorModel
from app.model.transaction import (TransactionList, Transaction, TransactionCreate, TransactionUpdate,
                                   TransactionTargetEnum,
                                   )
from app.router.shop import get_shop_by_account
from app.utils.auth import get_current_active_user, if_shop_owns_product
from app.utils.db_process import get_all_results, execute_query
from app.utils.transaction_formatter import get_transactions

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
        account_uuid: str | None = None,
        target: TransactionTargetEnum = TransactionTargetEnum.Account
):
    """
    Get transaction list of current logged in account.
    :param account:  Current logged in account
    :param account_uuid: Admins may provide an account_uuid to get transaction list of that account.
    :param target:  (TransactionTargetEnum): [description]. Defaults to TransactionTargetEnum.Account.
         Valid Value: {Account, Shop}
    :return: TransactionList
    :raises HTTPException 401: Unauthorized, HTTPException 403: Forbidden,    HTTPException 404: Not found
    """
    if account_uuid:
        if account.role != 1:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )
    else:
        account_uuid = account.account_uuid

    if target == TransactionTargetEnum.Shop:
        condition = f"WHERE T.shop_uuid = (SELECT shop_uuid FROM Shop WHERE account_uuid = '{account_uuid}')"
    else:
        condition = f"WHERE T.account_uuid = '{account_uuid}'"

    return get_transactions(condition)

@router.get(
    path="/all",
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
async def get_all_transaction_list(
        account: Annotated[
            Account,
            Depends(get_current_active_user)],
):
    """
    Get transaction list of all accounts.
    :param account: Current logged in account
    :return: TransactionList
    :raises HTTPException 401: Unauthorized, HTTPException 403: Forbidden,    HTTPException 404: Not found
    """
    if account.role != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )

    return get_transactions()

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
    Create a transaction.
    :param account: Current logged in account
    :param transaction: TransactionCreate
    :return: Transaction

    :raises HTTPException 401: Unauthorized, HTTPException 403: Forbidden,    HTTPException 404: Not found
    """
    if len(transaction.products.transaction_product_logs) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No product in transaction",
        )

    transaction_uuid = str(uuid.uuid4())
    values: list[list] = []

    for product in transaction.products.transaction_product_logs:
        if not await if_shop_owns_product(shop_uuid=transaction.shop_uuid, product_uuid=product.product_uuid):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There's an impostor among the transaction products",
            )
        values.append(
            [
                transaction_uuid,
                product.product_uuid,
                product.quantity
            ]
        )

    account_uuid = account.account_uuid

    sql = """
    INSERT INTO 
    Transaction (transaction_uuid, account_uuid, shop_uuid,coupon_uuid, receive_time, status) 
    VALUES (%s, %s,%s,
    (SELECT coupon_uuid FROM Coupon WHERE coupon_code = %s)
    , %s, %s)
    """
    transaction_values = (
        transaction_uuid,
        account_uuid,
        transaction.shop_uuid,
        transaction.coupon_code,
        transaction.receive_time,
        transaction.status.value
    )

    result: bool = execute_query(sql, transaction_values)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Transaction failed",
        )

    try:
        sql = """
            INSERT INTO 
            TransactionProductLog (transaction_uuid, product_uuid, quantity) 
            VALUES   """

        for value in values:
            sql += f"('{value[0]}', '{value[1]}', {value[2]}),"
        sql = sql[:-1]

        execute_query(sql)

        sql = f"""
            UPDATE Product
            JOIN (
                SELECT TPL.product_uuid, SUM(TPL.quantity) as total_quantity
                FROM TransactionProductLog TPL
                WHERE TPL.transaction_uuid = '{transaction_uuid}'
                GROUP BY TPL.product_uuid
            ) AS ProductQuantities ON Product.product_uuid = ProductQuantities.product_uuid
            SET Product.stock = Product.stock - ProductQuantities.total_quantity
            """
        execute_query(sql)

        return TransactionCreate(
            shop_uuid=transaction.shop_uuid,
            receive_time=transaction.receive_time,
            status=transaction.status,
            products=transaction.products,
            coupon_code=transaction.coupon_code
        )
    except Exception as e:
        sql = "DELETE FROM NFT.Transaction WHERE transaction_uuid LIKE %s ESCAPE '#'"
        execute_query(sql, (transaction_uuid,))
        sql = "DELETE FROM NFT.TransactionProductLog WHERE transaction_uuid LIKE %s ESCAPE '#'"
        execute_query(sql, (transaction_uuid,))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Transaction failed: " + str(e)
        )

@router.put(
    path="/{transaction_uuid}",
    responses={
        status.HTTP_200_OK: {
            "model": TransactionUpdate
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
async def update_transaction(
        account: Annotated[
            Account,
            Depends(get_current_active_user)],
        transaction: TransactionUpdate = Depends(TransactionUpdate.as_form)
):
    """
    Update a transaction. Admins may provide an account_uuid to update a transaction for that account.
    :param account: Current logged in account
    :param transaction: TransactionUpdate
    :return: TransactionUpdate

    :raises HTTPException 401: Unauthorized, HTTPException 403: Forbidden,    HTTPException 404: Not found
    """

    sql = "SELECT * FROM Transaction WHERE transaction_uuid = %s"
    result: Dict = get_all_results(sql, (transaction.transaction_uuid,))
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found",
        )
    if account.role != 1 and result[0]["shop_uuid"] != (await get_shop_by_account(account)).shop_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )

    sql = """
    UPDATE Transaction
    SET receive_time = %s, status = %s
    WHERE transaction_uuid = %s
    """
    values = (
        transaction.receive_time,
        transaction.status,
        transaction.transaction_uuid,
    )

    result: bool = execute_query(sql, values)
    if result:
        return TransactionUpdate(
            receive_time=transaction.receive_time,
            status=transaction.status,
            transaction_uuid=transaction.transaction_uuid
        )
