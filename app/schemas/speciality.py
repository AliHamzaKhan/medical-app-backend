from pydantic import BaseModel
from typing import Optional


class SpecialityBase(BaseModel):
    name: str


class SpecialityCreate(SpecialityBase):
    pass

class SpecialityUpdate(SpecialityBase):
    name: Optional[str] = None

class Speciality(SpecialityBase):
    id: int

    class Config:
        from_attributes = True
