import uuid
from typing import Annotated, Dict

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.model.account import Account
from app.model.general import ErrorModel
from app.model.transaction import (TransactionList, Transaction, TransactionCreate, TransactionUpdate,
                                   TransactionTargetEnum, TransactionProductLog, TransactionProductLogList,
                                   )
from app.router.shop import get_shop_by_account
from app.utils.auth import get_current_active_user, if_shop_owns_product
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

    sql = f"""
        SELECT T.*, TPL.product_uuid, TPL.quantity, P.price
        FROM 
        Transaction T 
        left join NFT.TransactionProductLog TPL 
        on T.transaction_uuid = TPL.transaction_uuid 
        left join NFT.Product P 
        on TPL.product_uuid = P.product_uuid
        """
    if target == TransactionTargetEnum.Shop:
        sql += "WHERE T.shop_uuid = (SELECT shop_uuid FROM Shop WHERE account_uuid = %s)"
    else:
        sql += "WHERE T.account_uuid = %s"

    results = get_all_results(sql, (account_uuid,))
    result = TransactionList(transactions=[])
    if results:
        i = 0
        while i < len(results):
            curr = Transaction(
                transaction_uuid=results[i]["transaction_uuid"],
                account_uuid=results[i]["account_uuid"],
                shop_uuid=results[i]["shop_uuid"],
                coupon_code=results[i]["coupon_code"],
                receive_time=results[i]["receive_time"],
                status=results[i]["status"],
                total_price=0,
                products=TransactionProductLogList(transaction_product_logs=[])
            )
            while i < len(results) and results[i]["transaction_uuid"] == curr.transaction_uuid:
                curr.products.transaction_product_logs.append(
                    TransactionProductLog(
                        product_uuid=results[i]["product_uuid"],
                        quantity=results[i]["quantity"],
                        price=results[i]["price"]
                    )
                )
                curr.total_price += results[i]["price"] * results[i]["quantity"]
                i += 1
            result.transactions.append(curr)
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Transaction not found",
    )

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

    sql = "SELECT * FROM Transaction"

    result = get_all_results(sql)

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

    account_uuid = transaction.account_uuid if transaction.account_uuid and account.role == 1 else account.account_uuid

    sql = """
    INSERT INTO 
    Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status) 
    VALUES (%s, %s, %s, %s, %s)
    """
    transaction_values = (
        transaction_uuid,
        account_uuid,
        transaction.coupon_code,
        transaction.receive_time,
        transaction.status.value
    )

    result: bool = execute_query(sql, transaction_values)

    sql = """
        INSERT INTO 
        TransactionProductLog (transaction_uuid, product_uuid, quantity) 
        VALUES (%s, %s, %s)
        """
    for value in values:
        execute_query(sql, tuple(value))

        return Transaction(
            transaction_uuid=transaction_uuid,
            account_uuid=account_uuid,
            shop_uuid=transaction.shop_uuid,
            coupon_code=transaction.coupon_code,
            receive_time=transaction.receive_time,
            status=transaction.status,
            products=transaction.products
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
        transaction_uuid: str,
        transaction: TransactionUpdate,
):
    """
    Update a transaction. Admins may provide an account_uuid to update a transaction for that account.
    :param account: Current logged in account
    :param transaction_uuid: Transaction uuid
    :param transaction: TransactionUpdate
    :return: TransactionUpdate

    :raises HTTPException 401: Unauthorized, HTTPException 403: Forbidden,    HTTPException 404: Not found
    """

    sql = "SELECT * FROM Transaction WHERE transaction_uuid = %s"
    result: Dict = get_all_results(sql, (transaction_uuid,))
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
        transaction_uuid,
    )

    result: bool = execute_query(sql, values)
    if result:
        return TransactionUpdate(
            receive_time=transaction.receive_time,
            status=transaction.status
        )
