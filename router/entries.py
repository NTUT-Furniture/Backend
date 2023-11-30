from fastapi import APIRouter

from .account import router as account_router
from .product import router as product_router
from .shop import router as shop_router

def register_router(app):
    router = APIRouter()
    router.include_router(account_router, prefix="/account")
    router.include_router(product_router, prefix="/product")
    router.include_router(shop_router, prefix="/shop")

    app.include_router(router, prefix="/api")
