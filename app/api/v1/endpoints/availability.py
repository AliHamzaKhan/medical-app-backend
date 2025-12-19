from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Availability)
def create_availability(
    *, 
    db: Session = Depends(deps.get_db),
    availability_in: schemas.AvailabilityCreate
):
    availability = crud.cavailability.create(db, obj_in=availability_in)
    return availability


@router.get("/", response_model=List[schemas.Availability])
def read_availabilities(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    availabilities = crud.cavailability.get_multi(db, skip=skip, limit=limit)
    return availabilities
