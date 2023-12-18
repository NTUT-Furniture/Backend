from fastapi import APIRouter

from .account import router as account_router
# from .image import router as image_router
# from .coupon import router as coupon_router
from .login import router as login_router
from .product import router as product_router
from .shop import router as shop_router

def register_router(app):
    router = APIRouter()
    router.include_router(account_router, prefix="/account")
    router.include_router(shop_router, prefix="/shop")
    router.include_router(product_router, prefix="/product")
    # router.include_router(image_router, prefix="/image")
    # router.include_router(coupon_router, prefix="/coupon")
    router.include_router(login_router)

    app.include_router(router, prefix="/api")
