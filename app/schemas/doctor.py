from pydantic import BaseModel
from typing import List

class DoctorBase(BaseModel):
    name: str
    specialization: str
    hospital_id: int

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(DoctorBase):
    pass

class DoctorInDB(DoctorBase):
    id: int

    class Config:
        orm_mode = True

class Doctor(DoctorInDB):
    pass
