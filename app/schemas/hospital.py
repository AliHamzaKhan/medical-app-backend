from pydantic import BaseModel, ConfigDict
from typing import Optional

class HospitalBase(BaseModel):
    name: str
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    departments: Optional[str] = None
    website: Optional[str] = None
    phone_no: Optional[str] = None
    current_status: Optional[str] = None
    image: Optional[str] = None
    timings: Optional[str] = None

class HospitalCreate(HospitalBase):
    address: str
    latitude: float
    longitude: float

class HospitalUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    departments: Optional[str] = None
    website: Optional[str] = None
    phone_no: Optional[str] = None
    current_status: Optional[str] = None
    image: Optional[str] = None
    timings: Optional[str] = None

class HospitalInDB(HospitalBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class Hospital(HospitalInDB):
    pass

class HospitalIdName(BaseModel):
    id: int
    name: str
