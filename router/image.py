from typing import Annotated

from fastapi import APIRouter, status, UploadFile, File, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import Account
from model.image import ImageUploadSuccessModel, ImageIOFailModel, ImageTypeModel
from utils import image_io, auth
from utils.db_process import if_exists_in_db

router = APIRouter(
    tags=["image", "product", "account", "shop"],
)

@router.post(
    "/upload",
    description="Upload image(jpeg/png) for product, max_size = 10MB",
    responses={
        status.HTTP_200_OK: {
            "model": ImageUploadSuccessModel
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ImageIOFailModel
        },
    },
    tags=["upload"]
)
async def upload_image(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        img_type: ImageTypeModel = ImageTypeModel.avatar,
        file: UploadFile = File(...)
):
    owner_uuid = account.account_uuid
    if img_type == ImageTypeModel.banner:
        if not await if_exists_in_db("Shop", "account_uuid", owner_uuid):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=jsonable_encoder(
                    {
                        "msg": f"No such shop: {owner_uuid}"
                    }
                )
            )
        return await image_io.save_file(file, owner_uuid, img_type)
    elif img_type == ImageTypeModel.avatar:
        if await if_exists_in_db("Account", "account_uuid", owner_uuid) or \
                await if_exists_in_db("Product", "product_uuid", owner_uuid) or \
                await if_exists_in_db("Shop", "shop_uuid", owner_uuid):
            return await image_io.save_file(file, owner_uuid, img_type)
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "msg": f"Image type must be avatar or banner! Get {img_type} instead!"
                }
            )
        )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "msg": f"No such owner: {owner_uuid}"
            }
        )
    )

@router.get(
    "/get_image/",
    description="Get image(jpeg/png) for account or product",
    responses={
        status.HTTP_200_OK: {
            "model": ImageUploadSuccessModel
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ImageIOFailModel
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ImageIOFailModel
        },
    },
    tags=["get"]
)
async def get_image(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        img_type: ImageTypeModel = ImageTypeModel.avatar
):
    owner_uuid = account.account_uuid
    if img_type == ImageTypeModel.banner:
        if not await if_exists_in_db("Shop", "shop_uuid", owner_uuid):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=jsonable_encoder(
                    {
                        "msg": f"No such shop: {owner_uuid}"
                    }
                )
            )
        return await image_io.get_file(owner_uuid, img_type)
    elif img_type == ImageTypeModel.avatar:
        if await if_exists_in_db("Account", "account_uuid", owner_uuid) or \
                await if_exists_in_db("Product", "product_uuid", owner_uuid) or \
                await if_exists_in_db("Shop", "shop_uuid", owner_uuid):
            return await image_io.get_file(owner_uuid, img_type)
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "msg": f"Image type must be avatar or banner! Get {img_type} instead!"
                }
            )
        )
