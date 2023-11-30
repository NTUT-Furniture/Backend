from router.Product.image import router as product_image_router

from router.Account.account import gather_all_routers as gather_all_account_routers

def register_router(app):
    for router in gather_all_account_routers():
        app.include_router(router)
    app.include_router(product_image_router)
