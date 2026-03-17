from functools import lru_cache
from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    app_name: str = "Trendsee Feed Service"
    secret_key: str = "change_me_in_production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24

    postgres_user: str = "trendsee"
    postgres_password: str = "trendsee"
    postgres_db: str = "trendsee"
    postgres_host: str = "db"
    postgres_port: int = 5432

    redis_url: AnyUrl | None = None

    # Optional artificial delay for "cold" (non-cached) data. Keep 0 for real speed.
    cold_delay_seconds: float = 0.0

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()

