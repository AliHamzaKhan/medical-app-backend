import random
import string
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.user import UserCreate


def random_lower_string(k: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=k))


def random_float() -> float:
    return random.random() * 100


def random_email() -> str:
    return f"{random_lower_string(8)}@{random_lower_string(8)}.com"


def get_superuser_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            first_name="Super",
            last_name="User",
            date_of_birth="1990-01-01",
            gender="male",
            phone_number="1234567890",
            address="123 Test St",
            role="superuser",
        )
        crud.user.create(db, obj_in=user_in)

    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
