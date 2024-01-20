from fastapi import HTTPException
import requests

from firebase_admin import firestore
from model.Settings import Settings

from model.User import User

from google.cloud.firestore import FieldFilter


def create_user(user: User):
    db = firestore.client()
    users_ref = db.collection("users")
    query_ref = users_ref.where(filter=FieldFilter("id", "==", user.uid))
    if 0 < len(query_ref.get()):
        raise HTTPException(
            status_code=422,
            detail="既に登録済みです",
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
