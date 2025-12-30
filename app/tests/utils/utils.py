import random
import string
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.init_db import init_db


def random_lower_string(k: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=k))


def random_email() -> str:
    return f"{random_lower_string(8)}@{random_lower_string(8)}.com"


def get_superuser_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    init_db(db)
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers

def random_float(min_val: float, max_val: float) -> float:
    return random.uniform(min_val, max_val)
