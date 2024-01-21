from firebase_admin import auth
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from model.Authorization import Authorization


def verify_id_token(authorization: Authorization):
    verify_id_token = auth.verify_id_token(authorization.token)
    return Authorization(uid=verify_id_token["uid"], token=authorization.token)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends((HTTPBearer())),
):
    authorization = Authorization.create(token=credentials.credentials)
    try:
        verified_token = verify_id_token(authorization)
        return verified_token
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error",
        ) from e
