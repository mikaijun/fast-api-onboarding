from functools import lru_cache
from typing import Annotated
from fastapi import APIRouter, Depends
import requests
from model.Settings import Settings
from firebase_admin import auth

router = APIRouter()

@lru_cache()
def get_settings():
    return Settings()

@router.get("/user/create", tags=["users"])
def user_create():
    user = auth.create_user(
    email='user@example.com',
    email_verified=False,
    phone_number='+15555550100',
    password='secretPassword',
    display_name='John Doe',
    photo_url='http://www.example.com/12345678/photo.png',
    disabled=False)
    return {"message": 'Sucessfully created new user: {0}'.format(user.uid)}

@router.get("/user/token", tags=["users"])
def get_token(settings: Annotated[Settings, Depends(get_settings)]):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={settings.api_key}"
    data = {"email": "user@example.com" , "password": "secretPassword", "returnSecureToken": True}
    result = requests.post(url=uri, data=data).json()
    return result["idToken"]
