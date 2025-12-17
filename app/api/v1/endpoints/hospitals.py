
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Hospital)
def create_hospital(
    *, 
    db: Session = Depends(deps.get_db), 
    hospital_in: schemas.HospitalCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new hospital.
    """
    hospital = crud.hospital.create(db, obj_in=hospital_in)
    return hospital


@router.get("/", response_model=List[schemas.Hospital])
def read_hospitals(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve hospitals.
    """
    hospitals = crud.hospital.get_multi(db, skip=skip, limit=limit)
    return hospitals
