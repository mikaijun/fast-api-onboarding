from pydantic_settings import BaseSettings
from firebase_admin import auth
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class User(BaseSettings):
    uid: str

    def create(uid):
        return User(uid=uid)

    def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        if not cred:
            raise HTTPException(
                status_code=402,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            cred = auth.verify_id_token(cred.credentials)
        except:
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return User(uid=cred["uid"])
