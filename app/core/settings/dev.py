from app.core.settings.base import BaseConfig

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = "postgresql://user@localhost:5432/health-app-db"
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
