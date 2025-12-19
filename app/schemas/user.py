from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import time, datetime

# Schemas for related models

class SpecialityBase(BaseModel):
    name: str

class SpecialityCreate(SpecialityBase):
    pass

class SpecialityUpdate(BaseModel):
    name: Optional[str] = None

class Speciality(SpecialityBase):
    id: int

    class Config:
        from_attributes = True

class DoctorDocumentBase(BaseModel):
    document_path: str

class DoctorDocumentCreate(DoctorDocumentBase):
    pass

class DoctorDocumentUpdate(BaseModel):
    document_path: Optional[str] = None

class DoctorDocument(DoctorDocumentBase):
    id: int

    class Config:
        from_attributes = True

class ClinicBase(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    consultation_fee: float
    start_time: time
    end_time: time

class ClinicCreate(ClinicBase):
    pass

class ClinicUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    consultation_fee: Optional[float] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None

class Clinic(ClinicBase):
    id: int

    class Config:
        from_attributes = True

class MedicineSearchHistoryBase(BaseModel):
    search_query: str
    timestamp: datetime
    user_id: int
    medicine_id: Optional[int] = None

class MedicineSearchHistoryCreate(MedicineSearchHistoryBase):
    pass

class MedicineSearchHistory(MedicineSearchHistoryBase):
    id: int

    class Config:
        from_attributes = True

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    full_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    
    # Patient fields
    phone: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    allergic_reaction: Optional[str] = None
    
    total_ai_credits: int = 10
    used_ai_credits: int = 0

    total_medicine_search_credits: int = 50
    used_medicine_search_credits: int = 0

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to receive via API on update
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    full_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    phone: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    allergic_reaction: Optional[str] = None
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True

# Additional properties to return via API
class User(UserInDBBase):
    remaining_ai_credits: int
    remaining_medicine_search_credits: int
    specialities: List[Speciality] = []
    documents: List[DoctorDocument] = []
    clinics: List[Clinic] = []
    medicine_search_history: List[MedicineSearchHistory] = []

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
