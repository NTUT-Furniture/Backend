# use uvicorn to run the server
# uvicorn main:app --reload
import uvicorn
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
app.add_api_route("/account", account.get_account)
if __name__ == "__main__":
    print(Settings['workers'])
    uvicorn.run(
        "main:app",
        host = Settings["host"], 
        port = Settings["port"],
        reload = True,
        workers = Settings["workers"],
    ) 