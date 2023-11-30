from fastapi import APIRouter

prefix = "/account"
router = APIRouter(
    prefix=prefix,
    tags=["account"],
)
