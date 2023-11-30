from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import status
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from model.image import ImageUploadSuccessModel, ImageIOFailModel
from utils import image_io
from utils.db_process import get_all_results

router = APIRouter(
    tags=["product"],
)

@router.post("/upload_image/{id}",
             description="Upload image(jpeg/png) for product, max_size = 10MB",
             responses={
                 status.HTTP_200_OK: {
                     "model": ImageUploadSuccessModel
                 },
                 status.HTTP_400_BAD_REQUEST: {
                     "model": ImageIOFailModel
                 }},
             tags=["product", "img_upload"]
             )
async def upload_image(id, file: UploadFile):
    script = """
    SELECT EXISTS(SELECT 1 FROM Product WHERE product_uuid = %s) AS UUID_Exists;
    """
    result = get_all_results(script, (id,))
    if result:
        return await image_io.save_file(file, image_io.ImgSourceEnum.product, id)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"msg": "No such product: " + id})
    )
