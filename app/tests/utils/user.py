import datetime
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.models.user import User
from app.schemas.user import UserCreate, User as UserSchema
from app.schemas.doctor import DoctorCreate
from app.tests.utils.utils import random_email, random_lower_string
from app.tests.utils.speciality import create_random_speciality
from app.tests.utils.clinic import create_random_clinic


def user_authentication_headers(
    *, client: TestClient, email: str, password: str
) -> Dict[str, str]:
    data = {"username": email, "password": password}

    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def create_random_user(db: Session, client: TestClient, is_superuser: bool = False) -> User:
    email = random_email()
    password = random_lower_string(8)
    role = "superuser" if is_superuser else "patient"
    user_in = UserCreate(
        email=email,
        password=password,
        first_name="Test",
        last_name="User",
        date_of_birth=datetime.date(1990, 1, 1),
        gender="male",
        phone_number="1234567890",
        address="123 Test St",
        role=role,
    )
    user = crud.user.create(db=db, obj_in=user_in)
    return user, password


def create_random_doctor(db: Session, client: TestClient) -> UserSchema:
    email = random_email()
    password = random_lower_string(8)
    user_in = UserCreate(
        email=email,
        password=password,
        first_name="Test",
        last_name="Doctor",
        date_of_birth=datetime.date(1980, 1, 1),
        gender="female",
        phone_number="0987654321",
        address="456 Test Ave",
        role="doctor",
    )
    user = crud.user.create(db=db, obj_in=user_in)
    
    speciality = create_random_speciality(db)
    clinic = create_random_clinic(db, client)

    doctor_in = DoctorCreate(
        user_id=user.id,
        years_of_experience=5,
        consultation_fee=100,
        bio="A test doctor",
    )
    doctor = crud.doctor.create(db, obj_in=doctor_in)
    doctor.specialities.append(speciality)
    db.commit()

    headers = user_authentication_headers(client=client, email=email, password=password)
    user.token = headers["Authorization"].split(" ")[1]
    return user


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
