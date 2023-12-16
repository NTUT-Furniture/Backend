from typing import Annotated

from fastapi import APIRouter, status, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.model.account import Account
from app.model.image import ImageUploadSuccessModel, ImageIOFailModel, ImageTypeModel
from app.utils import image_io
from app.utils import auth
from app.utils.auth import if_account_owns_shop, if_account_owns_product
from app.utils.db_process import if_exists_in_db

router = APIRouter(
    tags=["image", "product", "account", "shop"],
)

async def handle_image_not_found(img_type, owner_uuid):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "msg": f"No {img_type} image found for owner: {owner_uuid}"
        }
    )

@router.post(
    "/",
    responses={
        status.HTTP_200_OK: {"model": ImageUploadSuccessModel},
        status.HTTP_404_NOT_FOUND: {"model": ImageIOFailModel},
        status.HTTP_400_BAD_REQUEST: {"model": ImageIOFailModel}
    }
)
async def upload_image(
        account: Annotated[Account, Depends(auth.get_current_active_user)],
        shop_uuid: str | None = None,
        product_uuid: str | None = None,
        img_type: ImageTypeModel = ImageTypeModel.avatar,
        file: UploadFile = File(...)
):
    if img_type == ImageTypeModel.banner:
        if shop_uuid is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Shop uuid is required for uploading a banner image"
            )
        if not await if_account_owns_shop(account.account_uuid, shop_uuid):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Account: {account.account_uuid} doesn't own shop: {shop_uuid}"
            )
        return await image_io.save_file(file, shop_uuid, img_type)
    elif img_type == ImageTypeModel.avatar:
        if product_uuid is None:
            if shop_uuid is None:
                return await image_io.save_file(file, account.account_uuid, img_type)
            elif await if_exists_in_db("Shop", "shop_uuid", shop_uuid):
                if not await if_account_owns_shop(account.account_uuid, shop_uuid):
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Account: {account.account_uuid} doesn't own shop: {shop_uuid}"
                    )
                return await image_io.save_file(file, shop_uuid, img_type)
        elif await if_exists_in_db("Product", "product_uuid", product_uuid):
            if not await if_account_owns_product(account.account_uuid, shop_uuid, product_uuid):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=f"Account: {account.account_uuid} doesn't own shop: {shop_uuid} or \
                    the shop doesn't own product: {product_uuid}"
                )
            return await image_io.save_file(file, product_uuid, img_type)

@router.get(
    "/{owner_uuid}",
    tags=["get"],
    responses={
        status.HTTP_200_OK: {"model": ImageUploadSuccessModel},
        status.HTTP_404_NOT_FOUND: {"model": ImageIOFailModel},
        status.HTTP_400_BAD_REQUEST: {"model": ImageIOFailModel}
    }
)
async def get_image(
        owner_uuid: str,
        img_type: ImageTypeModel = ImageTypeModel.avatar,
):
    if img_type == ImageTypeModel.banner:
        if not await if_exists_in_db("Shop", "shop_uuid", owner_uuid):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Shop uuid: {owner_uuid} doesn't exist!"
            )
    return await image_io.get_file(owner_uuid, img_type)
