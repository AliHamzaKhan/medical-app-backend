
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI")
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 # 8 days
    SECRET_KEY: str = os.getenv("SECRET_KEY")

settings = Settings()
