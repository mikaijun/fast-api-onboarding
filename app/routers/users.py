from typing import Union
from functools import lru_cache
from typing import Annotated
from fastapi import APIRouter, Depends, Header
from repository import get_current_user
from repository.users import create_user, firebase_login
from model.Settings import Settings

router = APIRouter()

@lru_cache()
def get_settings():
    return Settings()

@router.get("/user", tags=["users"])
# def user_get(cred: Union[str, None] = Header(default=None)):
def user_get(cred = Depends(get_current_user)):
    uid = cred.get("uid")
    return {"message": f"Hello, {uid}!"}

@router.get("/user/create", tags=["users"])
def user_create():
    create_user()
    # TODO: returnの変更
    return {"message": 'Sucessfully created new user'}

@router.get("/user/login", tags=["users"])
def login(settings: Annotated[Settings, Depends(get_settings)]):
    # TODO: firebase以外の認証方法に切り替えた場合はメソッドを変更する
    return firebase_login(settings.api_key)
