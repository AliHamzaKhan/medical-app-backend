from pydantic import BaseModel, ConfigDict
from typing import Optional


class SpecialityBase(BaseModel):
    name: str


class SpecialityCreate(SpecialityBase):
    pass

class SpecialityUpdate(SpecialityBase):
    name: Optional[str] = None

class Speciality(SpecialityBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
