from typing import Optional

from pydantic_settings import BaseSettings


class Authentication(BaseSettings):
    token: str
    uid: Optional[str] = None
