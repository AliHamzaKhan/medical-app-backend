from pydantic import BaseModel
from .user import User

class PatientBase(BaseModel):
    pass

class PatientCreate(PatientBase):
    user_id: int

class Patient(PatientBase):
    id: int
    user: User

    class Config:
        orm_mode = True
