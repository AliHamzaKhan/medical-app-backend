from pydantic import BaseModel

class PharmacistBase(BaseModel):
    name: str | None = None
    hospital_id: int | None = None
    license_number: str | None = None

class PharmacistCreate(PharmacistBase):
    name: str

class PharmacistUpdate(PharmacistBase):
    pass

class PharmacistInDBBase(PharmacistBase):
    id: int
    name: str
    owner_id: int

    class Config:
        from_attributes = True

class Pharmacist(PharmacistInDBBase):
    pass

class PharmacistInDB(PharmacistInDBBase):
    pass
