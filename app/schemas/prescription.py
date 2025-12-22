from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

# Shared properties
class PrescriptionBase(BaseModel):
    medication_name: Optional[str] = None
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    notes: Optional[str] = None


# Properties to receive on item creation
class PrescriptionCreate(PrescriptionBase):
    appointment_id: int
    medication_name: str
    dosage: str
    frequency: str
    start_date: date


# Properties to receive on item update
class PrescriptionUpdate(PrescriptionBase):
    pass


# Properties shared by models in DB
class PrescriptionInDBBase(PrescriptionBase):
    id: int
    appointment_id: int

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Prescription(PrescriptionInDBBase):
    pass


# Properties properties stored in DB
class PrescriptionInDB(PrescriptionInDBBase):
    pass
