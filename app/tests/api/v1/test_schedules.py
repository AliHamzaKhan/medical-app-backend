from typing import Dict
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.core.config import settings
from app.tests.utils.user import create_random_doctor
from app.tests.utils.appointment import create_random_appointment
from app.models.user import User


def test_get_doctor_schedule_today(
    client: TestClient, db: Session, superuser_token_headers: Dict[str, str]
) -> None:
    doctor = create_random_doctor(db, client)
    # Create an appointment for today
    appointment_today = create_random_appointment(db, client=client, doctor_id=doctor.id, appointment_time=datetime.utcnow())
    # Create an appointment for tomorrow
    create_random_appointment(
        db, client=client, doctor_id=doctor.id, appointment_time=datetime.utcnow() + timedelta(days=1)
    )

    r = client.get(
        f"{settings.API_V1_STR}/schedules/doctors/{doctor.id}", headers=superuser_token_headers
    )
    assert r.status_code == 200
    appointments = r.json()
    assert len(appointments) == 1
    assert appointments[0]["id"] == appointment_today.id
