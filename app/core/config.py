from functools import lru_cache
from typing import List, Tuple
from pydantic_settings import BaseSettings, SettingsConfigDict
import logging
import os

ENV: str = os.getenv("APP_ENV", "")


class Settings(BaseSettings):
    # base
    APP_ENV: str = ENV
    DEBUG: bool = False
    DOCS_URL: str = "/docs"
    OPENAPI_PREFIX: str = ""
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    TITLE: str = "fastapi clean template"
    VERSION: str = "0.0.1"

    DB_ENGINE_MAPPER: dict = {
        "postgresql": "postgresql",
        "mysql": "mysql+pymysql",
        "mongodb": "mongodb",
    }
    DB: str = "postgresql"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_USER: str = ""
    DB_NAME: str = ""
    DB_PASSWORD: str = ""
    DB_ENGINE: str = DB_ENGINE_MAPPER[DB]
    DB_URI: str = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # auth
    SECRET_KEY: str = "secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10  # 10 mins
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 30 * 24 * 60  # 30 days
    OTP_INTERVAL: int = 30

    API_PREFIX: str = "/api"

    # CORS
    ALLOW_CREDENTIALS: bool = True
    ALLOW_HOSTS: List[str] = ["*"]
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]
    DISALLOW_AGENTS: List[str] = [
        "zgrab",
        "curl",
        "wget",
        "postmanruntime",
        "python-requests",
    ]

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    # find query
    DEFAULT_PAGE_SIZE: int = 50
    MAX_PAGE_SIZE: int = 100

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env" if "dev" == ENV else ".env.prod" if "prod" == ENV else ".env.test",
    )


settings = Settings()
