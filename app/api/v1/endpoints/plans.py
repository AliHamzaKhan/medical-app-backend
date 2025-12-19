from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Plan)
def create_plan(
    *, 
    db: Session = Depends(deps.get_db),
    plan_in: schemas.PlanCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new plan.
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    plan = crud.crud_plan.create_plan(db=db, plan_in=plan_in)
    return plan


@router.get("/", response_model=List[schemas.Plan])
def read_plans(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve plans.
    """
    plans = crud.crud_plan.get_plans(db, skip=skip, limit=limit)
    return plans
