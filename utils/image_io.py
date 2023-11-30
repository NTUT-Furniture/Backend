import os
import shutil
from typing import Optional, Union
from uuid import uuid4

from fastapi import UploadFile, status
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse, FileResponse

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def list_files(dir_path: str) -> list[str]:
    files_list = [os.path.join(root, file) for root, _, files in os.walk(dir_path) for file in files]
    return files_list

def get_directory_path(owner_id: str) -> str:
    path = f"../upload_images/{owner_id}"
    return path

def get_filename(file: UploadFile) -> str:
    _, filetype = file.filename.split(".")
    new_filename = str(uuid4())
    return f"{new_filename}.{filetype}"

async def save_file(file: Optional[UploadFile], owner_id: str) -> JSONResponse:
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
        filename = get_filename(file)
        with open(os.path.join(directory_path, filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=f"Error when saving file: {e}"
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "success",
            "image_uuid": filename.split(".")[0],
            "size": file.size
        })
    )

async def get_file(owner_uuid: str, file_uuid: str) -> Union[FileResponse, JSONResponse]:
    directory_path = get_directory_path(owner_uuid)
    if not os.path.exists(directory_path):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({
                "msg": f"uuid {owner_uuid} haven't upload any image yet"
            })
        )

    files_list = list_files(directory_path)
    for file in files_list:
        if file_uuid in file:
            return FileResponse(file)

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({
            "msg": "No such file"
        })
    )
