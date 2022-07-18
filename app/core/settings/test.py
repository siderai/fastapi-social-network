import logging

from app.core.settings.app import AppSettings
from pydantic import PostgresDsn, SecretStr


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "(Test) Social Network app based on FastAPI"

    secret_key: SecretStr = SecretStr("test_secret")

    database_url: PostgresDsn
    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG
