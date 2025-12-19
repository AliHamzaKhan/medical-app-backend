from typing import Optional
from pydantic import BaseModel
from .user import User

class PatientBase(BaseModel):
    pass

class PatientCreate(PatientBase):
    user_id: int

class PatientUpdate(PatientBase):
    user_id: Optional[int] = None

class Patient(PatientBase):
    id: int
    user: User

    class Config:
        from_attributes = True
