from sqlalchemy.orm import Session

from app import crud
from app.schemas.plan import PlanCreate

def create_random_plan(db: Session) -> None:
    plan_in = PlanCreate(
        name="Test Plan",
        description="Test Description",
        price=49.99,
        duration_days=30
    )
    return crud.plan.create(db=db, obj_in=plan_in)
