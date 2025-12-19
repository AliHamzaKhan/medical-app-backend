from pydantic import BaseModel


class SpecialityBase(BaseModel):
    name: str


class SpecialityCreate(SpecialityBase):
    pass


class Speciality(SpecialityBase):
    id: int

    class Config:
        orm_mode = True
