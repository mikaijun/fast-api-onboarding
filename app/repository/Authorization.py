from firebase_admin import auth
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from model.Authorization import Authorization


def verify_id_token(authorization: Authorization):
    try:
        verify_id_token = auth.verify_id_token(authorization.token)
    except:
        raise HTTPException(
            status_code=401,
            detail="ユーザー認証に失敗しました",
        )
    return Authorization(uid=verify_id_token["uid"], token=authorization.token)


def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if not cred:
        raise HTTPException(
            status_code=401,
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
