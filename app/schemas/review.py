from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Shared properties
class ReviewBase(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None
    review_date: Optional[datetime] = None


# Properties to receive on item creation
class ReviewCreate(ReviewBase):
    doctor_id: int
    patient_id: int
    rating: int


# Properties to receive on item update
class ReviewUpdate(ReviewBase):
    pass


# Properties shared by models in DB
class ReviewInDBBase(ReviewBase):
    id: int
    doctor_id: int
    patient_id: int

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Review(ReviewInDBBase):
    pass


# Properties properties stored in DB
class ReviewInDB(ReviewInDBBase):
    pass
