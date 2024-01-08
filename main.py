import sys
import firebase_admin

from typing import Annotated
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from firebase_admin import auth, credentials
import requests


sys.path.append("./dependencies")
from firebase_admin import credentials

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# サーバーの起動
app = FastAPI()

# リクエストボディの定義
class Message(BaseModel):
  name: str

class Settings(BaseSettings):
    api_key: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings():
    return Settings()

# 認証関数の定義
def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if not cred:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    try:
        cred = auth.verify_id_token(cred.credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return cred

# getを定義
@app.get("/hello")
def read_root(cred = Depends(get_current_user)):
    uid = cred.get("uid")
    return {"message": f"Hello, {uid}!"}

# postを定義
@app.post("/hello")
def create_message(message: Message, cred = Depends(get_current_user)):
    uid = cred.get("uid")
    return {"message": f"Hello, {message.name}! Your uid is [{uid}]"}

@app.get("/user/create")
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

@app.get("/user/token")
def get_token(settings: Annotated[Settings, Depends(get_settings)]):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={settings.api_key}"
    data = {"email": "user@example.com" , "password": "secretPassword", "returnSecureToken": True}
    result = requests.post(url=uri, data=data).json()
    return result["idToken"]
