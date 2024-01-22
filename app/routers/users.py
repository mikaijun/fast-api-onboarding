from typing import List, Union

from fastapi import APIRouter, Depends, Header, HTTPException

from model.authentication import Authentication
from model.user import User
from repository.authentication import AuthRepository
from repository.user import UserRepository
from services.authUser import AuthUserService

router = APIRouter()
user_repository = UserRepository()
authentication_repository = AuthRepository()
authUserService = AuthUserService()
auth_user = authUserService.get_auth_user


@router.get("/user", tags=["users"])
async def user_get(auth_user: Authentication = Depends(auth_user)):
    return auth_user


@router.post("/user/create", tags=["users"])
# NOTE: Headerに関しては以下を参照
# see: https://fastapi.tiangolo.com/ja/tutorial/header-params/#_3
def user_create(x_token: Union[List[str], None] = Header(default=None)):
    try:
        authentication = authentication_repository.verify_id_token(
            Authentication(token=x_token[0])
        )
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="ユーザー認証に失敗しました",
        )
    new_user = User(id=authentication.uid)
    already_user = user_repository.find(new_user)
    if already_user is not None:
        raise HTTPException(
            status_code=409,
            detail="既に登録済みのユーザーです",
        )
    return user_repository.create_user(new_user)
