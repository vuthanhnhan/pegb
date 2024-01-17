from functools import wraps
from typing import Callable
from fastapi import Request, HTTPException
import time
from jose import jwt
import os 

def require_permission(handler: Callable[..., dict]):
    @wraps(handler)
    async def wrapper(request: Request, *args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        try:
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
            timestamp = time.time()
            if timestamp > payload.get('expire'):
                raise HTTPException(status_code=401, detail="Could not validate credentials")

            request.state.payload = payload
        except Exception:
            raise HTTPException(status_code=401, detail="Could not validate credentials")

        return await handler(request, *args, **kwargs)
    return wrapper
