from pydantic import BaseModel
from datetime import time, date

class AvailabilityBase(BaseModel):
    doctor_id: int
    clinic_id: int
    date: date
    start_time: time
    end_time: time
    is_booked: bool = False

class AvailabilityCreate(AvailabilityBase):
    pass

class AvailabilityUpdate(BaseModel):
    is_booked: bool

class AvailabilityInDB(AvailabilityBase):
    id: int

    class Config:
        from_attributes = True

class Availability(AvailabilityInDB):
    pass
