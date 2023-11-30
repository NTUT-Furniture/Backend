from fastapi import UploadFile
from fastapi import status

from model.image_io import ImageIOSuccessModel, ImageIOFailModel
from router.Product.product import router
from utils import image_io

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
    flag = await image_io.save_file(file, image_io.ImgSourceEnum.product, id)
    return {"filename": file.filename, "content_type": file.content_type, "size": file.size, "success": flag}
