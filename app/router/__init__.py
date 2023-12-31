from fastapi import APIRouter

from .account import router as account_router
from .coupon import router as coupon_router
from .image import router as image_router
from .login import router as login_router
from .product import router as product_router
from .shop import router as shop_router
from .subscription import router as subscription_router
from .transaction import router as transaction_router
from .comment import router as comment_router

def register_router(app):
    router = APIRouter()
    router.include_router(account_router, prefix="/account")
    router.include_router(shop_router, prefix="/shop")
    router.include_router(product_router, prefix="/product")
    router.include_router(image_router, prefix="/image")
    router.include_router(coupon_router, prefix="/coupon")
    router.include_router(login_router)
    router.include_router(subscription_router, prefix="/subscription")
    router.include_router(transaction_router, prefix="/transaction")
    router.include_router(comment_router, prefix="/comment")

    app.include_router(router, prefix="/api")
