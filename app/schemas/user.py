from pydantic import BaseModel
from datetime import date
from typing import List
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

class User(UserBase):
    id: int
    specialities: List[Speciality] = []

    class Config:
        orm_mode = True
