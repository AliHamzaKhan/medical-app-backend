from pydantic import BaseModel
from datetime import datetime
from .doctor import Doctor
from .patient import Patient

class ReviewBase(BaseModel):
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    doctor_id: int
    patient_id: int

class Review(ReviewBase):
    id: int
    review_date: datetime
    doctor: Doctor
    patient: Patient

    class Config:
        orm_mode = True
