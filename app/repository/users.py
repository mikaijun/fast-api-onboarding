import statistics
from fastapi import HTTPException
import requests

from firebase_admin import auth, firestore

from model.User import User


def create_user(user: User):
    db = firestore.client()
    collections = db.collection("users").stream()
    # TODO: リファクタ
    # TODO: リクエストされたuuidとfirebaseのuuidが一致するか確認する
    for doc in collections:
        if doc.id == user.uid:
            raise HTTPException(
                status_code=422,
                detail="登録済みです",
            )
    doc_ref = db.collection("users").document(user.uid)
    doc_ref.set({"id": user.uid})
    return User(uid=user.uid)


def firebase_login(api_key: str):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={api_key}"
    data = {
        "email": "user@example.com",
        "password": "secretPassword",
        "returnSecureToken": True,
    }
    result = requests.post(url=uri, data=data).json()
    return result["idToken"]
