from pydantic import BaseModel


class ClinicBase(BaseModel):
    name: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class ClinicCreate(ClinicBase):
    name: str


class ClinicUpdate(ClinicBase):
    pass


class ClinicInDBBase(ClinicBase):
    id: int
    name: str
    owner_id: int

    class Config:
        from_attributes = True


class Clinic(ClinicInDBBase):
    pass


class ClinicInDB(ClinicInDBBase):
    pass
