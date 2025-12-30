from typing import Optional

from pydantic import BaseModel, ConfigDict


class MedicineBase(BaseModel):
    description: Optional[str] = None
    requires_prescription: Optional[bool] = False
    price: Optional[float] = None


class MedicineCreate(MedicineBase):
    name: str
    manufacturer: str
    dosage: str
    price: float


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
