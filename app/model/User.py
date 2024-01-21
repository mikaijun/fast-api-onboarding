from pydantic_settings import BaseSettings


class User(BaseSettings):
    uid: str

    def create(uid):
        return User(uid=uid)
