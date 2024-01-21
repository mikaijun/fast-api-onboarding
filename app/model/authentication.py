from typing import Optional

from pydantic_settings import BaseSettings


class Authentication(BaseSettings):
    token: str
    uid: Optional[str] = None

    def from_token(token):
        return Authentication(token=token)
