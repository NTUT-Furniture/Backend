from typing import Annotated

from fastapi import APIRouter, status, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse

from model.account import Account
from model.image import ImageUploadSuccessModel, ImageIOFailModel, ImageTypeModel
from utils import image_io, auth
from utils.db_process import if_exists_in_db

router = APIRouter(
    tags=["image", "product", "account", "shop"],
)

async def handle_image_not_found(img_type, owner_uuid):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "msg": f"Image type must be avatar or banner! Get {img_type} instead!"
        }
    )

async def is_image_available(account_uuid):
    return await if_exists_in_db("Account", "account_uuid", account_uuid) or \
        await if_exists_in_db("Product", "product_uuid", account_uuid) or \
        await if_exists_in_db("Shop", "shop_uuid", account_uuid)

@router.post(
    "/upload",
    responses={
        status.HTTP_200_OK: {"model": ImageUploadSuccessModel},
        status.HTTP_404_NOT_FOUND: {"model": ImageIOFailModel},
        status.HTTP_400_BAD_REQUEST: {"model": ImageIOFailModel}
    }
)
async def upload_image(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        img_type: ImageTypeModel = ImageTypeModel.avatar, file: UploadFile = File(...)
):
    owner_uuid = account.account_uuid
    if img_type == ImageTypeModel.banner:
        if not await if_exists_in_db("Shop", "account_uuid", owner_uuid):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Account {owner_uuid} has no shop!"
            )
        return await image_io.save_file(file, owner_uuid, img_type)
    elif img_type == ImageTypeModel.avatar and await is_image_available(owner_uuid):
        return await image_io.save_file(file, owner_uuid, img_type)
    return handle_image_not_found(img_type, owner_uuid)

@router.get(
    "/get_image/",
    responses={
        status.HTTP_200_OK: {"model": ImageUploadSuccessModel},
        status.HTTP_404_NOT_FOUND: {"model": ImageIOFailModel},
        status.HTTP_400_BAD_REQUEST: {"model": ImageIOFailModel}
    }
)
async def get_image(
        account: Annotated[
            Account, Depends(auth.get_current_active_user)],
        img_type: ImageTypeModel = ImageTypeModel.avatar
):
    owner_uuid = account.account_uuid
    if img_type == ImageTypeModel.banner:
        if not await if_exists_in_db("Shop", "account_uuid", owner_uuid):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No shops under account: {owner_uuid}"
            )
        return await image_io.get_file(owner_uuid, img_type)
    elif img_type == ImageTypeModel.avatar and await is_image_available(owner_uuid):
        return await image_io.get_file(owner_uuid, img_type)
    else:
        return handle_image_not_found(img_type, owner_uuid)
