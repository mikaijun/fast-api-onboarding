from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """envファイルの設定を読み込むクラス

    see: https://fastapi.tiangolo.com/ru/advanced/settings/
    """

    api_key: str
    model_config = SettingsConfigDict(env_file="../.env")
