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
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Create new plan.
    """
    plan = crud.plan.create(db=db, obj_in=plan_in)
    return plan


@router.get("/", response_model=List[schemas.Plan])
def read_plans(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve plans.
    """
    plans = crud.plan.get_multi(db, skip=skip, limit=limit)
    return plans

@router.get("/{id}", response_model=schemas.Plan)
def read_plan(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get plan by ID.
    """
    plan = crud.plan.get(db=db, id=id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan
