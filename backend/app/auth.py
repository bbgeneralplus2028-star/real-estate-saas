from jose import jwt
from datetime import datetime, timedelta
import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
ALGORITHM = "HS256"

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=7)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
