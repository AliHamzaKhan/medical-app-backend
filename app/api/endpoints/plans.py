from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Plan)
def create_plan(
    *, 
    db: Session = Depends(get_db), 
    plan_in: schemas.PlanCreate
) -> Any:
    plan = crud.plan.create(db=db, obj_in=plan_in)
    db.commit()
    db.refresh(plan)
    return plan

@router.get("/", response_model=List[schemas.Plan])
def read_plans(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    plans = crud.plan.get_multi(db, skip=skip, limit=limit)
    return plans

@router.get("/{id}", response_model=schemas.Plan)
def read_plan(
    *, 
    db: Session = Depends(get_db), 
    id: int
) -> Any:
    plan = crud.plan.get(db=db, id=id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan
