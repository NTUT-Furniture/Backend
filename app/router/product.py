import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from app.model.account import Account
from app.model.general import ErrorModel
from app.model.product import (CreateProductForm, Product, CreateProductResponse,
                               UpdateProductForm, UpdateProductResponse, ProductList, GetProductForm, OrderEnum,
                               )
from app.utils import auth
from app.utils.db_process import (get_all_results, execute_query, dict_to_sql_command, dict_delete_none,
                                  get_shop_by_account_uuid,
                                  )
from app.utils.product_getter import *

router = APIRouter(
    tags=["product"]
)

@router.get(
    path="/",
    tags=["get"],
    responses={
        status.HTTP_200_OK: {
            "model": Product
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_product(
        shop_uuid: str,
):
    sql = """
        SELECT * FROM `Product` WHERE shop_uuid = %s;
    """
    result = get_all_results(sql, (shop_uuid,))
    if result:
        return ProductList(products=result)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no product for shop_uuid {shop_uuid}"
    )

@router.post(
    "/", tags=["create"], responses={
        status.HTTP_200_OK: {
            "model": CreateProductResponse
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def create_product(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        product_form: CreateProductForm = Depends(CreateProductForm.as_form)
):
    shop_uuid = await get_shop_by_account_uuid(account.account_uuid)
    product_form = product_form.model_dump()
    product_form["is_active"] = product_form["is_active"] if product_form["is_active"] is not None else 1
    product_id = str(uuid.uuid4())
    sql = """
        INSERT INTO `Product`
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, DEFAULT);
    """
    result = execute_query(sql, (product_id, shop_uuid, *product_form.values()))
    if result:
        return CreateProductResponse(shop_uuid=shop_uuid, product_uuid=product_id, **product_form)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Create Product failed."
    )

@router.put(
    "/", tags=["update"], responses={
        status.HTTP_200_OK: {
            "model": UpdateProductResponse
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorModel
        }
    }
)
async def update_product(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        product_form: UpdateProductForm = Depends(UpdateProductForm.as_form)
):
    """
    example:
    asd@gmail.com
    123

    product_uuid: 094527b3-f8f1-4dfc-82cb-066a48d29caa
    """
    product_uuid = product_form.product_uuid
    sql = """
        SELECT EXISTS(SELECT 1
        FROM `Product` P, `Shop` S, `Account` A
        WHERE P.shop_uuid = S.shop_uuid
        AND S.account_uuid = A.account_uuid
        AND P.product_uuid = %s
        AND A.account_uuid = %s) AS Exist;
    """
    result = get_all_results(sql, (product_uuid, account.account_uuid))
    if not result[0]['Exist']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorModel(
                msg=f"Account {account.account_uuid} does not own product {product_uuid}"
            )
        )
    product_form = product_form.model_dump()
    product_form = dict_delete_none(product_form)
    sql_set_text, sql_set_values = dict_to_sql_command(product_form, exclude_col=["product_uuid"])
    sql = f"""
        UPDATE `Product` SET {sql_set_text}
        WHERE product_uuid = %s;
    """
    result = execute_query(sql, (sql_set_values + (product_form["product_uuid"],)))
    if result:
        return UpdateProductResponse(product_uuid=product_form["product_uuid"])
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Update product failed."
    )

@router.get(
    path="/all",
    tags=["get"],
    responses={
        status.HTTP_200_OK: {
            "model": ProductList
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel
        }
    }
)
async def get_all_products(
        product_form: GetProductForm = Depends(GetProductForm.as_form),
        order: OrderEnum = OrderEnum.random
):
    """
    Get all products with filter and order.
    Query parameters' default values and meanings:
    - order:
        - default: random
        - available: product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time, random
        - meaning: order by the column
    - shop_uuid:
        - default: None
        - available: any shop_uuid
        - meaning: filter by shop_uuid
    - is_active:
        - default: 1
        - available: 0, 1
        - meaning: filter by is_active
    - from_price:
        - default: 0
        - available: any unsigned  integer
        - meaning: filter by price >= from_price
    - to_price:
        - default: 4294967295
        - available: any unsigned integer
        - meaning: filter by price <= to_price
    - from_stock:
        - default: 0
        - available: any unsigned integer
        - meaning: filter by stock >= from_stock
    - to_stock:
        - default: 4294967295
        - available: any unsigned integer
        - meaning: filter by stock <= to_stock
    - tags:
        - default: None
        - available: any string
        - meaning: filter by tags
    - start:
        - default: 0
        - available: any unsigned integer
        - meaning: start from the start-th product
    - limit:
        - default: 10
        - available: any unsigned integer
        - meaning: limit the number of products
    """
    product_form = product_form.model_dump()
    product_form = dict_delete_none(product_form)
    product_form = GetProductForm(**product_form)

    sql = f"""
        SELECT * FROM `Product` WHERE 
    """
    sql += filter_by("price", min_value=product_form.from_price, max_value=product_form.to_price) + " AND "
    sql += filter_by("stock", min_value=product_form.from_stock, max_value=product_form.to_stock) + " AND "
    if product_form.shop_uuid is not None:
        sql += filter_by("shop_uuid", value=product_form.shop_uuid) + " AND "
    if product_form.is_active is not None:
        sql += filter_by("is_active", value=product_form.is_active) + " AND "
    if product_form.tags is not None:
        sql += filter_by("tags", value=product_form.tags) + " AND "

    sql = sql[:-5]

    if order is not None:
        sql += order_by(order.value)

    sql += interval(product_form.start, product_form.limit)

    result = get_all_results(sql)

    if result:
        return ProductList(products=result)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There is no product."
    )
