import os
import shutil
from typing import Optional, Union

from fastapi import UploadFile, status
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse, FileResponse

from model.account import Account
from model.image import ImageTypeModel

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def if_exists(file_path: str, target_filename: str) -> Union[None, str]:
    for filename in os.listdir(file_path):
        if os.path.splitext(filename)[0] == target_filename:
            return os.path.splitext(filename)[1]
    return None

def get_directory_path(owner_id: str) -> str:
    path = f"../upload_images/{owner_id}"
    return path

def get_filename(file: UploadFile, image_type: ImageTypeModel) -> str:
    _, filetype = file.filename.split(".")
    return f"{image_type.value}.{filetype}"

async def save_file(file: Optional[UploadFile], owner_id: str, image_type: ImageTypeModel) -> JSONResponse:
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(
            status_code=400,
            content=f"File must be jpeg or png format! Get {file.content_type} instead!"
        )
    if file.size > MAX_FILE_SIZE:
        return JSONResponse(
            status_code=400,
            content=f"File size must be less than 10MB! The file uploaded is  {file.size} Bytes!"
        )
    try:
        directory_path = get_directory_path(owner_id)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        filename = get_filename(file, image_type)
        with open(os.path.join(directory_path, filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=f"Error when saving file: {e}"
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(
            {
                "msg": "success",
                "owner_uuid": f"{owner_id}",
                "image_type": f"{image_type.value}",
                "size": f"{file.size}Bytes",
            }
        )
    )

async def get_file(owner_uuid: str, image_type: ImageTypeModel) -> Union[FileResponse, JSONResponse]:
    directory_path = get_directory_path(owner_uuid)
    if not os.path.exists(directory_path):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder(
                {
                    "msg": f"uuid {owner_uuid} haven't upload any image yet"
                }
            )
        )
    ext = if_exists(directory_path, image_type)
    if ext is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder(
                {
                    "msg": f"uuid {owner_uuid} haven't upload {image_type.value} yet"
                }
            )
        )
    return FileResponse(f"{directory_path}/{image_type.value}{ext}")

def get_owner_uuid(account: Account, shop_uuid: str | None = None, product_uuid: str | None = None):
    if product_uuid is not None:
        return product_uuid
    elif shop_uuid is not None:
        return shop_uuid
    else:
        return account.account_uuid
