from pydantic import BaseModel
from typing import Optional

class HospitalBase(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    departments: Optional[str] = None
    website: Optional[str] = None
    phone_no: Optional[str] = None
    current_status: Optional[str] = None
    image: Optional[str] = None
    timings: Optional[str] = None

class HospitalCreate(HospitalBase):
    pass

class HospitalUpdate(HospitalBase):
    pass

class HospitalInDB(HospitalBase):
    id: int

    class Config:
        orm_mode = True

class Hospital(HospitalInDB):
    pass
