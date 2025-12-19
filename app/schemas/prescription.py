from pydantic import BaseModel
from datetime import date
from .appointment import Appointment

class PrescriptionBase(BaseModel):
    medication_name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: date
    notes: str

class PrescriptionCreate(PrescriptionBase):
    appointment_id: int

class Prescription(PrescriptionBase):
    id: int
    appointment: Appointment

    class Config:
        from_attributes = True
