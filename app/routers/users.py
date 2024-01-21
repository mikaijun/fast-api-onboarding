from typing import List, Union

from fastapi import APIRouter, Depends, Header, HTTPException

from model.auth import Auth
from model.user import User
from repository.auth import AuthRepository
from repository.user import UserRepository

router = APIRouter()
user_repository = UserRepository()
authentication_repository = AuthRepository()


@router.get("/user", tags=["users"])
async def user_get(
    current_user: Auth = Depends(authentication_repository.get_current_user),
):
    return current_user


@router.post("/user/create", tags=["users"])
# NOTE: Headerに関しては以下を参照
# see: https://fastapi.tiangolo.com/ja/tutorial/header-params/#_3
def user_create(x_token: Union[List[str], None] = Header(default=None)):
    try:
        verified_token = authentication_repository.verify_id_token(
            Auth.create(token=x_token[0])
        )
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="ユーザー認証に失敗しました",
        )
    new_user = User.create(verified_token.uid)
    already_user = user_repository.find_user_by_uid(new_user)
    if already_user is not None:
        raise HTTPException(
            status_code=409,
            detail="既に登録済みのユーザーです",
        )
    return user_repository.create_user(new_user)
