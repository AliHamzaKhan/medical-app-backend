from app.core.settings.base import BaseConfig

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
