from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Availability)
def create_availability(
    *, 
    db: Session = Depends(deps.get_db),
    availability_in: schemas.AvailabilityCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new availability.
    """
    availability = crud.availability.create(db=db, obj_in=availability_in)
    return availability


@router.get("/", response_model=List[schemas.Availability])
def read_availabilities(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Retrieve availabilities.
    """
    availabilities = crud.availability.get_multi(db, skip=skip, limit=limit)
    return availabilities


@router.get("/{id}", response_model=schemas.Availability)
def read_availability(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get availability by ID.
    """
    availability = crud.availability.get(db=db, id=id)
    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found")
    return availability


@router.put("/{id}", response_model=schemas.Availability)
def update_availability(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    availability_in: schemas.AvailabilityUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update an availability.
    """
    availability = crud.availability.get(db=db, id=id)
    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found")
    availability = crud.availability.update(db=db, db_obj=availability, obj_in=availability_in)
    return availability


@router.delete("/{id}", response_model=schemas.Availability)
def delete_availability(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Delete an availability.
    """
    availability = crud.availability.get(db=db, id=id)
    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found")
    availability = crud.availability.remove(db=db, id=id)
    return availability
