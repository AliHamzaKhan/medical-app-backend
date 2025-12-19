from pydantic import BaseModel

class StaffBase(BaseModel):
    name: str | None = None
    hospital_id: int | None = None
    role: str | None = None

class StaffCreate(StaffBase):
    name: str

class StaffUpdate(StaffBase):
    pass

class StaffInDBBase(StaffBase):
    id: int
    name: str
    owner_id: int

    class Config:
        from_attributes = True

class Staff(StaffInDBBase):
    pass

class StaffInDB(StaffInDBBase):
    pass
