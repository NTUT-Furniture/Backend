from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.settings import Settings
from router import account

app = FastAPI(
    title = "FastAPI Demo",
    description = "FastAPI Demo",
    version = "0.0.1",
    docs_url = Settings["api_docs"],
    openapi_url = Settings["api_prefix"] + Settings["api_docs"],
)

app.add_middleware(CORSMiddleware)
app.include_router(account.router, prefix = Settings["api_prefix"])
