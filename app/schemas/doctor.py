from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from .user import User
from app.models.doctor import DoctorStatus

class DoctorBase(BaseModel):
    years_of_experience: int
    consultation_fee: int
    bio: str

class DoctorCreate(DoctorBase):
    user_id: int

class DoctorUpdate(DoctorBase):
    years_of_experience: Optional[int] = None
    consultation_fee: Optional[int] = None
    bio: Optional[str] = None
    user_id: Optional[int] = None

class DoctorStatusUpdate(BaseModel):
    status: DoctorStatus

class Doctor(DoctorBase):
    id: int
    user: User
    specialities: List[str] = []
    status: DoctorStatus

    model_config = ConfigDict(from_attributes=True)
