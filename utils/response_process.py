from typing import Optional, Union

from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def send_response(
        msg: str,
        status_code: status = status.HTTP_200_OK,
        data: Union[Optional[dict], str] = "",
):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder({
            "msg": msg,
            "data": data
        })
    )
