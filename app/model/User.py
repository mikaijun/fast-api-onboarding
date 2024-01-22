from pydantic_settings import BaseSettings


class User(BaseSettings):
    id: str
