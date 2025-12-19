
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings

def create_initial_superuser(db: Session) -> None:
    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)

def create_initial_plans(db: Session) -> None:
    plans = crud.crud_plan.get_plans(db)
    if not plans:
        plan_in = schemas.PlanCreate(
            name="Basic",
            price=0.00,
            duration_days=30,
        )
        crud.crud_plan.create_plan(db, plan_in=plan_in)

        plan_in = schemas.PlanCreate(
            name="Premium",
            price=10.00,
            duration_days=30,
        )
        crud.crud_plan.create_plan(db, plan_in=plan_in)
