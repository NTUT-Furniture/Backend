from fastapi import HTTPException
from starlette import status

from app.model.transaction import TransactionList, Transaction, TransactionProductLogList, TransactionProductLog
from app.utils.db_process import get_all_results

def get_transactions(condition: str = "") -> TransactionList:
    sql = f"""
        SELECT T.transaction_uuid,
           T.account_uuid,
           T.shop_uuid,
           T.receive_time,
           T.status,
           T.order_time,
           C.discount,
           TPL.product_uuid,
           TPL.quantity,
           P.name,
           P.price,
           P.description
        from Transaction T
         left join NFT.TransactionProductLog TPL on T.transaction_uuid = TPL.transaction_uuid
         left join NFT.Product P on TPL.product_uuid = P.product_uuid
         left join Coupon C on T.coupon_uuid = C.coupon_uuid
        """ + condition
    results = get_all_results(sql)
    result = TransactionList(transactions=[])
    if results:
        i = 0
        while i < len(results):
            curr = Transaction(
                total_price=0,
                products=TransactionProductLogList(transaction_product_logs=[]),
                **results[i]
            )
            curr.discount = curr.discount / 100 if curr.discount is not None else 1
            while i < len(results) and results[i]["transaction_uuid"] == curr.transaction_uuid:
                curr.products.transaction_product_logs.append(
                    TransactionProductLog(
                        product_uuid=results[i]["product_uuid"],
                        product_name=results[i]["name"],
                        product_description=results[i]["description"],
                        quantity=results[i]["quantity"],
                        price=results[i]["price"]
                    )
                )
                curr.total_price += results[i]["price"] * results[i]["quantity"] * curr.discount
                i += 1
            result.transactions.append(curr)
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Transaction not found",
    )
