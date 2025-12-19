from pydantic import BaseModel
from typing import List
from .user import User

class DoctorBase(BaseModel):
    experience_years: int
    consultation_fee: int
    bio: str

class DoctorCreate(DoctorBase):
    user_id: int

class Doctor(DoctorBase):
    id: int
    user: User
    specialities: List[str] = []

    class Config:
        orm_mode = True
