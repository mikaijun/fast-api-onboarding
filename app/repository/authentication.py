from firebase_admin import auth

from model.authentication import Authentication


class AuthRepository:
    def verify_id_token(self, authorization: Authentication):
        verify_id_token = auth.verify_id_token(authorization.token)
        return Authentication(uid=verify_id_token["uid"], token=authorization.token)
