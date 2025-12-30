from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.testclient import TestClient

from app import crud, models
from app.schemas.appointment import AppointmentCreate
from app.tests.utils.user import create_random_user


def create_random_appointment(
    db: Session, *, client: TestClient, doctor_id: int, appointment_time: datetime
) -> models.Appointment:
    patient, _ = create_random_user(db, client)
    appointment_in = AppointmentCreate(
        doctor_id=doctor_id,
        patient_id=patient.id,
        appointment_time=appointment_time,
        status="scheduled",
    )
    return crud.appointment.create(db=db, obj_in=appointment_in)
