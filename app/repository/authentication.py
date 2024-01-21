from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth

from model.authentication import Authentication


class AuthRepository:
    def verify_id_token(self, authorization: Authentication):
        verify_id_token = auth.verify_id_token(authorization.token)
        return Authentication(uid=verify_id_token["uid"], token=authorization.token)

    async def get_current_user(
        self, credentials: HTTPAuthorizationCredentials = Depends((HTTPBearer()))
    ):
        authorization = Authentication.from_token(token=credentials.credentials)
        try:
            verified_token = self.verify_id_token(authorization)
            return verified_token
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error") from e
