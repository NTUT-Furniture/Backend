import os
import shutil
from datetime import datetime
from enum import Enum
from typing import Optional

from fastapi import UploadFile

class ImgSourceEnum(str, Enum):
    avatar = "avatar"
    product = "product"

def list_files(dir_path: str) -> list:
    files_list = [os.path.join(root, file) for root, _, files in os.walk(dir_path) for file in files]
    return files_list

def get_directory_path(whom: ImgSourceEnum, id: str) -> str:
    path = f"../upload_images/{whom.value}/{id}"
    return path

def get_filename(file: UploadFile) -> str:
    filename, filetype = file.filename.split(".")
    new_filename = f"{filename}_{datetime.now().timestamp()}"
    return f"{new_filename}.{filetype}"

async def save_file(file: Optional[UploadFile], whom: ImgSourceEnum, id: str) -> bool:
    try:
        directory_path = get_directory_path(whom, id)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        filename = get_filename(file)
        with open(os.path.join(directory_path, filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except (OSError, shutil.Error) as e:
        # LOG_ERROR(f"Error copying file: {e}")  TODO: the logger system
        return False
    except (FileNotFoundError, PermissionError) as e:
        # LOG_ERROR(f"Error copying file: {e}")
        return False
    return True
