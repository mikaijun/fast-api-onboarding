from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth

from model.auth import Auth


class AuthRepository:
    def verify_id_token(self, authorization: Auth):
        verify_id_token = auth.verify_id_token(authorization.token)
        return Auth(uid=verify_id_token["uid"], token=authorization.token)

    async def get_current_user(
        self, credentials: HTTPAuthorizationCredentials = Depends((HTTPBearer()))
    ):
        authorization = Auth.create(token=credentials.credentials)
        try:
            verified_token = self.verify_id_token(authorization)
            return verified_token
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error") from e
