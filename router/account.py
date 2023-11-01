from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from model.account import modelExample
from fastapi.responses import JSONResponse
router = APIRouter()

@router.get("/account", tags=["example"], responses={
    status.HTTP_200_OK: {
        "model": modelExample
    },
    })
async def get_account():
    return JSONResponse(content={"status": "success", "message": "Hello World"}
                        )


# id: int
#     name: str
#     email: str
#     password: str