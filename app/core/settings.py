import configparser
import os
from typing import Final

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'env.ini'))

Settings: Final = {
    "host": os.getenv("HOST"),
    "port": int(os.getenv("PORT")),
    "workers": int(os.getenv("WORKERS")),
    "api_prefix": str(config["SERVER"]["api_prefix"]),
    "api_docs": str(config["SERVER"]["api_docs"]),
    "api_redoc": str(config["SERVER"]["api_redoc"]),
    "access_token_expire_minutes": int(config["JWT"]["access_token_expire_minutes"]),
}
