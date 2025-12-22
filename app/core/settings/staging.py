import os
from app.core.settings.base import BaseConfig

class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = os.getenv("STAGING_DATABASE_URI")
