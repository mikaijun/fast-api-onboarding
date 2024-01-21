from typing import Optional

from pydantic_settings import BaseSettings


class Auth(BaseSettings):
    token: str
    uid: Optional[str] = None

    def create(token):
        return Auth(token=token)
