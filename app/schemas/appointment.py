from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AppointmentBase(BaseModel):
    patient_id: int
    availability_id: int
    appointment_time: datetime
    reason: str
    status: str

class AppointmentCreate(AppointmentBase):
    doctor_id: int
    start_time: datetime
    end_time: datetime

class AppointmentUpdate(BaseModel):
    patient_id: Optional[int] = None
    availability_id: Optional[int] = None
    appointment_time: Optional[datetime] = None
    reason: Optional[str] = None
    status: Optional[str] = None

class AppointmentInDB(AppointmentBase):
    id: int

    class Config:
        orm_mode = True

class Appointment(AppointmentInDB):
    pass
