from functools import lru_cache
from typing import Annotated, List, Union
from fastapi import APIRouter, Depends, Header
from fastapi.security import HTTPAuthorizationCredentials
from model.Authorization import Authorization
from repository.Authorization import verify_id_token
from repository.users import create_user, firebase_login
from model.Settings import Settings
from model.User import User

router = APIRouter()


@lru_cache()
def get_settings():
    return Settings()


@router.get("/user", tags=["users"])
def user_get(
    cred: Annotated[HTTPAuthorizationCredentials, Depends(User.get_current_user)]
) -> User:
    return cred


@router.post("/user/create", tags=["users"])
# NOTE: Headerに関しては以下を参照
# see: https://fastapi.tiangolo.com/ja/tutorial/header-params/#_3
def user_create(x_token: Union[List[str], None] = Header(default=None)):
    verified_token = verify_id_token(Authorization.create(token=x_token[0]))
    return create_user(User.create(verified_token.uid))


@router.get("/user/login", tags=["users"])
def login(
    settings: Annotated[Settings, Depends(get_settings)],
    _: Annotated[HTTPAuthorizationCredentials, Depends(User.get_current_user)],
):
    # TODO: firebase以外の認証方法に切り替えた場合はメソッドを変更する
    return firebase_login(settings.api_key)
