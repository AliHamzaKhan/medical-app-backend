import os
from dotenv import load_dotenv
from app.core.settings.base import BaseConfig
from app.core.settings.dev import DevConfig
from app.core.settings.staging import StagingConfig
from app.core.settings.production import ProdConfig

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "dev")

def get_settings():
    if APP_ENV == "dev":
        return DevConfig()
    elif APP_ENV == "staging":
        return StagingConfig()
    elif APP_ENV == "production":
        return ProdConfig()
    return BaseConfig()

settings = get_settings()
