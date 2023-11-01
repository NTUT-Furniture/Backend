import fastapi
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

router = APIRouter()

@router.get("/account")
async def get_account():
    return {"account": "account"}
