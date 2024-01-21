from pydantic_settings import BaseSettings


class User(BaseSettings):
    id: str

    def create(id):
        return User(id=id)
