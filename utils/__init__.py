from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from core.settings import Settings
from datetime import datetime, timedelta
from jose import JWTError, jwt
from os import getenv
import pytz
