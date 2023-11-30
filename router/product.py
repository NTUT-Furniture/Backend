from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import status

from model.image_io import ImageIOSuccessModel, ImageIOFailModel
from utils import image_io

router = APIRouter(
    tags=["product"],
)

@router.post("/{id}/upload_image",
             description="Upload image(jpeg/png) for product, max_size = 10MB",
             responses={
                 status.HTTP_200_OK: {
                     "model": ImageIOSuccessModel
                 },
                 status.HTTP_400_BAD_REQUEST: {
                     "model": ImageIOFailModel
                 }},
             tags=["product", "img_upload"]
             )
async def upload_image(id, file: UploadFile):
    return await image_io.save_file(file, image_io.ImgSourceEnum.product, id)
