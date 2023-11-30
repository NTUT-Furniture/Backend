from fastapi import APIRouter

from router.Account.create import router as create_router
from router.Account.get import router as get_router
from router.Account.image import router as image_router
from router.Account.update import router as update_router




def gather_all_routers() -> list[APIRouter]:
    return [create_router, get_router, image_router, update_router]
