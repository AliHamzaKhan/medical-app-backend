from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Schedule)
def create_schedule(
    *, 
    db: Session = Depends(deps.get_db), 
    schedule_in: schemas.ScheduleCreate, 
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Create new schedule.
    """
    doctor = crud.user.get(db, id=schedule_in.doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    schedule = crud.schedule.create(db=db, obj_in=schedule_in)
    return schedule


@router.get("/doctors/{doctor_id}")
def get_doctor_schedule_today(
    doctor_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Retrieve doctor's schedule for today.
    """
    today = date.today()
    start_of_day = datetime.combine(today, datetime.min.time())
    end_of_day = datetime.combine(today, datetime.max.time())

    appointments = crud.appointment.get_multi_by_doctor(
        db,
        doctor_id=doctor_id,
        start_time=start_of_day,
        end_time=end_of_day,
    )
    return appointments
