from pydantic import BaseModel
from datetime import date
from .user import User

class MedicalHistoryBase(BaseModel):
    diagnosis: str
    treatment: str
    visit_date: date

class MedicalHistoryCreate(MedicalHistoryBase):
    user_id: int

class MedicalHistory(MedicalHistoryBase):
    id: int
    user: User

    class Config:
        from_attributes = True
