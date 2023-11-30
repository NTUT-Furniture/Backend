from fastapi import UploadFile, APIRouter

from utils import image_io

prefix = "/account"
router = APIRouter(
    prefix=prefix,
    tags=["account", "get"],
)

@router.post("/{id}/upload_image",
             description="Upload image(jpeg/png) for product, max_size = 10MB",
             status_code=201,
             tags=["account", "img_upload"]
             )
async def upload_image(id, file: UploadFile):
    flag = await image_io.save_file(file, image_io.ImgSourceEnum.avatar, id)
    return {"filename": file.filename, "content_type": file.content_type, "size": file.size, "success": flag}

@router.get("/{id}/get_image",
            description="Get image(jpeg/png) for product",
            status_code=200,
            tags=["account", "img_get"]
            )
async def get_image(id):
    pass
