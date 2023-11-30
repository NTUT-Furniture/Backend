from fastapi import APIRouter

prefix = "/product"
router = APIRouter(
    prefix=prefix,
    tags=["product"],
)
