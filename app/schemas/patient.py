from pydantic import BaseModel
from datetime import date

class PatientBase(BaseModel):
    name: str
    date_of_birth: date
    address: str
    hospital_id: int

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class PatientInDB(PatientBase):
    id: int

    class Config:
        orm_mode = True

class Patient(PatientInDB):
    pass
