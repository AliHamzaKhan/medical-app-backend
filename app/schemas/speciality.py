from pydantic import BaseModel


class SpecialityBase(BaseModel):
    name: str | None = None


class SpecialityCreate(SpecialityBase):
    name: str


class SpecialityUpdate(SpecialityBase):
    pass


class SpecialityInDBBase(SpecialityBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class Speciality(SpecialityInDBBase):
    pass


class SpecialityInDB(SpecialityInDBBase):
    pass
