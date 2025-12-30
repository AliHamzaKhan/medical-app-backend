from app.core.settings.base import BaseConfig
from typing import List

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "password"

    class Config:
        env_file = ".env"
