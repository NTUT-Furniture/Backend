from router.Account.image import router as account_image_router
from router.Product.image import router as product_image_router


def register_router(app):
    app.include_router(account_image_router)
    app.include_router(product_image_router)
