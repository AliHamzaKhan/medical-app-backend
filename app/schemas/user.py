from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from app.models.user import UserRole
from .speciality import Speciality

class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone_number: str
    address: str
    role: UserRole

class UserCreate(UserBase):
    password: str
    speciality_ids: List[int] = []

class UserUpdate(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    role: Optional[UserRole] = None
    password: Optional[str] = None
    speciality_ids: Optional[List[int]] = []

class User(UserBase):
    id: int
    specialities: List[Speciality] = []

    class Config:
        from_attributes = True
