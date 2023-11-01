import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'env.ini'))

Settings = {
    "host": str(config["SERVER"]["host"]),
    "port": int(config["SERVER"]["port"]),
    "workers": int(config["SERVER"]["workers"]),
    "api_prefix": str(config["SERVER"]["api_prefix"]),
    "api_docs" : str(config["SERVER"]["api_docs"]),
}
