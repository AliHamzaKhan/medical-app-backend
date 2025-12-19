from pydantic import BaseModel
from typing import Optional

class MedicineBase(BaseModel):
    name: str
    formula: str
    side_effects: Optional[str] = None
    used_for: Optional[str] = None
    dosage_usage: Optional[str] = None

class MedicineCreate(MedicineBase):
    pass

class Medicine(MedicineBase):
    id: int

    class Config:
        orm_mode = True

class MedicineForDoctor(Medicine):
    alternatives: Optional[str] = None
    dose_calculator_info: Optional[str] = None
