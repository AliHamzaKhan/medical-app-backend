import datetime
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.models.user import User
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def user_authentication_headers(
    *, client: TestClient, email: str, password: str
) -> Dict[str, str]:
    data = {"username": email, "password": password}

    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def create_random_user(db: Session) -> (User, str):
    email = random_email()
    password = random_lower_string(8)
    user_in = UserCreate(
        email=email,
        password=password,
        first_name="Test",
        last_name="User",
        date_of_birth=datetime.date(1990, 1, 1),
        gender="male",
        phone_number="1234567890",
        address="123 Test St",
        role="patient",
    )
    user = crud.user.create(db=db, obj_in=user_in)
    return user, password
