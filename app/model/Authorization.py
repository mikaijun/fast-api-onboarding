from typing import Optional
from pydantic_settings import BaseSettings


class Authorization(BaseSettings):
    token: str
    uid: Optional[str] = None

    def create(token):
        return Authorization(token=token)
