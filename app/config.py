from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_HOST: str = Field(alias='POSTGRES_HOST')
    DB_PORT: str = Field(alias='POSTGRES_PORT')
    DB_NAME: str = Field(alias='POSTGRES_DB')
    DB_USER: str = Field(alias='POSTGRES_USER')
    DB_PASS: str = Field(alias='POSTGRES_PASSWORD')
    DB_DRIVER: str = "postgresql"

    @property
    def DATABASE_URL(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='.env')


config = Config()
