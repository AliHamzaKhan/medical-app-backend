
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_patients(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser_or_doctor),
) -> Any:
    """
    Retrieve patients.
    """
    patients = crud.patient.get_multi(db, skip=skip, limit=limit)
    return patients


@router.post("/", response_model=schemas.User)
def create_patient(
    *,
    db: Session = Depends(deps.get_db),
    patient_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new patient.
    """
    user = crud.user.get_by_email(db, email=patient_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    patient = crud.patient.create(db, obj_in=patient_in)
    return patient
