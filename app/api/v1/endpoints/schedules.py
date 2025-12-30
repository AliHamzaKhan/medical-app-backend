from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Schedule)
def create_schedule(
    *, 
    db: Session = Depends(deps.get_db),
    schedule_in: schemas.ScheduleCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    Create new schedule.
    """
    schedule = crud.schedule.create(db, obj_in=schedule_in)
    return schedule


@router.get("/", response_model=List[schemas.Schedule])
def read_schedules(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Retrieve schedules.
    """
    schedules = crud.schedule.get_multi(db, skip=skip, limit=limit)
    return schedules

@router.get("/doctor/{doctor_id}", response_model=List[schemas.Schedule])
def read_doctor_schedules(
    doctor_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Retrieve doctor's schedules.
    """
    schedules = db.query(models.Schedule).filter(models.Schedule.doctor_id == doctor_id).all()
    return schedules
