from functools import lru_cache
from typing import Annotated
from fastapi import APIRouter, Depends
from repository.users import create_user, firebase_login
from model.Settings import Settings

router = APIRouter()

@lru_cache()
def get_settings():
    return Settings()

@router.get("/user/create", tags=["users"])
def user_create():
    create_user()
    # TODO: returnの変更
    return {"message": 'Sucessfully created new user'}

# NOTE: エンドポイントに「user」が含まれてないが、ログインは認証関連のためusersに含める
@router.get("/login", tags=["users"])
def login(settings: Annotated[Settings, Depends(get_settings)]):
    # TODO: firebase以外の認証方法に切り替えた場合はメソッドを変更する
    return firebase_login(settings.api_key)
