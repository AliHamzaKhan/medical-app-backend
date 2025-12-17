
from pydantic import BaseModel

# Shared properties
class HospitalBase(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float

# Properties to receive on hospital creation
class HospitalCreate(HospitalBase):
    pass

# Properties to receive on hospital update
class HospitalUpdate(HospitalBase):
    pass

# Properties shared by models stored in DB
class HospitalInDBBase(HospitalBase):
    id: int

    class Config:
        orm_mode = True

# Properties to return to client
class Hospital(HospitalInDBBase):
    pass

# Properties properties stored in DB
class HospitalInDB(HospitalInDBBase):
    pass
