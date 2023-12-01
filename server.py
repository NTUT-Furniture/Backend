from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import Settings
from router import register_router

app = FastAPI(
    title="NFT API",
    description="NTUT furniture trading API",
    version="0.0.1",
    redoc_url=Settings["api_redoc"],
    docs_url=Settings["api_docs"],
    openapi_url=Settings["api_prefix"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_router(app)
