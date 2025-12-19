from pydantic import BaseModel
from datetime import datetime
from .user import User
from .doctor import Doctor
from .patient import Patient
from typing import Optional

class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_time: datetime
    status: str

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(AppointmentBase):
    doctor_id: Optional[int] = None
    patient_id: Optional[int] = None
    appointment_time: Optional[datetime] = None
    status: Optional[str] = None

class Appointment(AppointmentBase):
    id: int
    doctor: Doctor
    patient: Patient

    class Config:
        from_attributes = True
