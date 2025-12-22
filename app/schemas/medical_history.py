from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

# Shared properties
class MedicalHistoryBase(BaseModel):
    condition: Optional[str] = None
    date_diagnosed: Optional[date] = None
    notes: Optional[str] = None


# Properties to receive on item creation
class MedicalHistoryCreate(MedicalHistoryBase):
    patient_id: int
    condition: str
    date_diagnosed: date


# Properties to receive on item update
class MedicalHistoryUpdate(MedicalHistoryBase):
    pass


# Properties shared by models in DB
class MedicalHistoryInDBBase(MedicalHistoryBase):
    id: int
    patient_id: int

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class MedicalHistory(MedicalHistoryInDBBase):
    pass


# Properties properties stored in DB
class MedicalHistoryInDB(MedicalHistoryInDBBase):
    pass
