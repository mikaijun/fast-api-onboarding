from typing import List, Union
from fastapi import APIRouter, Depends, Header
from model.Authorization import Authorization
from repository.Authorization import get_current_user, verify_id_token
from repository.users import create_user
from model.User import User

router = APIRouter()


@router.get("/user", tags=["users"])
async def user_get(current_user: Authorization = Depends(get_current_user)):
    return current_user


@router.post("/user/create", tags=["users"])
# NOTE: Headerに関しては以下を参照
# see: https://fastapi.tiangolo.com/ja/tutorial/header-params/#_3
def user_create(x_token: Union[List[str], None] = Header(default=None)):
    verified_token = verify_id_token(Authorization.create(token=x_token[0]))
    return create_user(User.create(verified_token.uid))
