from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import Settings
from app.router import register_router

app = FastAPI(
    title="NFT API",
    description="NTUT furniture trading API",
    version="0.0.1",
    redoc_url=Settings["api_redoc"],
    docs_url=Settings["api_docs"],
    openapi_url=Settings["api_prefix"],
)

origins = [
    "http://localhost:5501",
    "http://localhost:63342",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_router(app)
