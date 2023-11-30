from fastapi import APIRouter, HTTPException
from fastapi import UploadFile
from fastapi import status
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

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
    try:
        new_file_name = await image_io.save_file(file, image_io.ImgSourceEnum.product, id)
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content=e.detail
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "success",
            "file_name": new_file_name,
            "size": file.size
        })
    )
