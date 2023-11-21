from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from typing import List, Optional
from model import image_io

prefix = "/product"
router = APIRouter(
    prefix=prefix,
    tags=["product"],
    responses={404: {"description": "Not found"}},
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

@router.post("/{id}/upload_image", description="Upload image(jpeg/png) for product, max_size = 10MB", status_code=201)
async def upload_image(id, file: UploadFile):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="File must be jpeg or png format!")
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size must be less than 10MB!")
    flag = await image_io.save_file(file, image_io.ImgSourceEnum.product, id)
    return {"filename": file.filename, "content_type": file.content_type, "size": file.size, "success": flag}
