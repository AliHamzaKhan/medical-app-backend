from pydantic import BaseModel, ConfigDict

class PlanBase(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    duration_days: int | None = None

class PlanCreate(PlanBase):
    name: str
    description: str
    price: float
    duration_days: int

class PlanUpdate(PlanBase):
    pass

class Plan(PlanBase):
    id: int
    name: str
    price: float
    duration_days: int

    model_config = ConfigDict(from_attributes=True)
