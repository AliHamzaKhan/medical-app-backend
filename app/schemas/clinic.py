from pydantic import BaseModel, ConfigDict


class ClinicBase(BaseModel):
    name: str | None = None
    address: str | None = None

class ClinicCreate(ClinicBase):
    name: str
    address: str


class ClinicUpdate(ClinicBase):
    pass


class ClinicInDBBase(ClinicBase):
    id: int
    name: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class Clinic(ClinicInDBBase):
    pass


class ClinicInDB(ClinicInDBBase):
    pass
