from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from model.authentication import Authentication
from model.user import User
from repository.authentication import AuthRepository
from repository.user import UserRepository

user_repository = UserRepository()
authentication_repository = AuthRepository()


class AuthUserService:
    async def get_auth_user(
        self, credentials: HTTPAuthorizationCredentials = Depends((HTTPBearer()))
    ):
        try:
            authentication = authentication_repository.verify_id_token(
                Authentication(token=credentials.credentials)
            )
        except Exception:
            raise HTTPException(
                status_code=401,
                detail="ユーザー認証に失敗しました",
            )
        user = user_repository.find(User(id=authentication.uid))
        if user is None:
            raise HTTPException(
                status_code=401,
                detail="ユーザーを取得できませんでした",
            )
        return user
