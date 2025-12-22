import os
from app.core.settings.base import BaseConfig

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = os.getenv("PROD_DATABASE_URI")
