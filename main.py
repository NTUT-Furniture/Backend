import uvicorn
from core.settings import Settings

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host=Settings["host"],
        port=Settings["port"],
        reload=True,
        workers=Settings["workers"],
	root_path=Settings["root_path"]
    )
