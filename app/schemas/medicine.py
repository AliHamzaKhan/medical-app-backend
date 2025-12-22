from typing import Optional

from pydantic import BaseModel, ConfigDict


class MedicineBase(BaseModel):
    description: Optional[str] = None


class MedicineCreate(MedicineBase):
    name: str
    manufacturer: str
    dosage: str


class MedicineUpdate(MedicineBase):
    pass


class MedicineInDBBase(MedicineBase):
    id: int
    name: str
    manufacturer: str
    dosage: str

    model_config = ConfigDict(from_attributes=True)


class Medicine(MedicineInDBBase):
    pass
