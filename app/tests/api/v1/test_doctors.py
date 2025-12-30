
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.core.config import settings
from app.tests.utils.user import create_random_doctor
from typing import Dict


def test_get_doctor_schedule(
    client: TestClient, db: Session, superuser_token_headers: Dict[str, str]
) -> None:
    doctor = create_random_doctor(db, client)
    response = client.get(f"{settings.API_V1_STR}/schedules/doctors/{doctor.id}", headers=superuser_token_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
