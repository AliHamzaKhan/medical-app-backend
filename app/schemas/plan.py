from pydantic import BaseModel

class PlanBase(BaseModel):
    name: str | None = None
    price: float | None = None
    duration_days: int | None = None

class PlanCreate(PlanBase):
    name: str
    price: float
    duration_days: int

class PlanUpdate(PlanBase):
    pass

class Plan(PlanBase):
    id: int
    name: str
    price: float
    duration_days: int

    class Config:
        orm_mode = True
