from typing import Optional

from pydantic import BaseModel


# Shared properties
class MedicineBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class MedicineCreate(MedicineBase):
    name: str


# Properties to receive on item update
class MedicineUpdate(MedicineBase):
    pass


# Properties shared by models stored in DB
class MedicineInDBBase(MedicineBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Medicine(MedicineInDBBase):
    pass


# Properties properties stored in DB
class MedicineInDB(MedicineInDBBase):
    pass
