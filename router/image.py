from fastapi import APIRouter, status, Depends, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.image import ImageUploadSuccessModel, ImageIOFailModel, ImageGetForm
from utils import image_io
from utils.db_process import if_exists_in_db

router = APIRouter(
    tags=["image", "product", "account"],
)

@router.post(
    "/upload/{owner_id}",
    description="Upload image(jpeg/png) for product, max_size = 10MB",
    responses={
        status.HTTP_200_OK: {"model": ImageUploadSuccessModel},
        status.HTTP_400_BAD_REQUEST: {"model": ImageIOFailModel},
    },
    tags=["upload"]
)
async def upload_image(owner_uuid: str, file: UploadFile = File(...)):
    if if_exists_in_db("Account", "account_uuid", owner_uuid) or \
            if_exists_in_db("Product", "product_uuid", owner_uuid):
        return await image_io.save_file(file, owner_uuid)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"msg": f"No such owner: {owner_uuid}"})
    )

@router.get(
    "/get_all_images/{owner_id}/all",
    description="Get all images(jpeg/png) for account or product",
    responses={
        status.HTTP_200_OK: {
            "model": ImageUploadSuccessModel
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ImageIOFailModel
        },
    },
    tags=["get", "get_all"]
)
async def get_all_images(owner_uuid: str):
    return await image_io.get_all_files(owner_uuid)

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
    },
    tags=["get", "product", "account"]
)
async def get_image(image_form: ImageGetForm = Depends(ImageGetForm.as_form)):
    return await image_io.get_file(image_form.owner_uuid, image_form.file_uuid)
