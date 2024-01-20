from typing import Union
from pydantic_settings import BaseSettings
from firebase_admin import auth
import statistics
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from grpc import Status


class User(BaseSettings):
    uid: str

    def create(uid):
        return User(uid=uid)

    def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        if not cred:
            raise HTTPException(
                status_code=statistics.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            cred = auth.verify_id_token(cred.credentials)
        except:
            raise HTTPException(
                status_code=Status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return User(uid=cred["uid"])
