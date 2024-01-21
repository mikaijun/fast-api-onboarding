from firebase_admin import firestore
from google.cloud.firestore import FieldFilter

from model.user import User


class UserRepository:
    def __init__(self):
        self.db = firestore.client()
        self.users_ref = self.db.collection("users")

    def create_user(self, user: User):
        doc_ref = self.users_ref.document(user.id)
        doc_ref.set({"id": user.id})
        return User(id=user.id)

    def find_user_by_uid(self, user: User):
        query_ref = self.users_ref.where(filter=FieldFilter("id", "==", user.id))
        result = query_ref.get()
        if 0 < len(result):
            return User(id=result[0].id)
        else:
            return None
