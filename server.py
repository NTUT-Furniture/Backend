from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.settings import Settings
from router import account, shop
from router.entries import register_router

app = FastAPI(
    title="NFT API",
    description="NTUT furniture trading API",
    version="0.0.1",
    docs_url=Settings["api_docs"],
    openapi_url=Settings["api_prefix"],
)

app.add_middleware(CORSMiddleware)
register_router(app)
