from firebase_admin import firestore

from model.User import User

from google.cloud.firestore import FieldFilter


def create_user(user: User):
    db = firestore.client()
    doc_ref = db.collection("users").document(user.id)
    doc_ref.set({"id": user.id})
    return User(id=user.id)


def find_user_by_uid(user: User):
    db = firestore.client()
    users_ref = db.collection("users")
    query_ref = users_ref.where(filter=FieldFilter("id", "==", user.id))
    if query_ref.get():
        return User(id=query_ref.get()[0].id)
    else:
        return None
