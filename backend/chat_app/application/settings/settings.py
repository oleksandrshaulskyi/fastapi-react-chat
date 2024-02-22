from os import path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_url: str

    model_config = SettingsConfigDict(env_file=path.join(path.dirname(__file__), '.env'))


settings = Settings()
