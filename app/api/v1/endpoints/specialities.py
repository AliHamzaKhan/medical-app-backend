from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Speciality])
def read_specialities(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve specialities.
    """
    specialities = crud.speciality.get_multi(db, skip=skip, limit=limit)
    return specialities


@router.post("/", response_model=schemas.Speciality)
def create_speciality(
    *, 
    db: Session = Depends(deps.get_db),
    speciality_in: schemas.SpecialityCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new speciality.
    """
    speciality = crud.speciality.create(db=db, obj_in=speciality_in)
    return speciality


@router.put("/{id}", response_model=schemas.Speciality)
def update_speciality(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    speciality_in: schemas.SpecialityUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a speciality.
    """
    speciality = crud.speciality.get(db=db, id=id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")
    speciality = crud.speciality.update(db=db, db_obj=speciality, obj_in=speciality_in)
    return speciality


@router.get("/{id}", response_model=schemas.Speciality)
def read_speciality(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get speciality by ID.
    """
    speciality = crud.speciality.get(db=db, id=id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")
    return speciality


@router.delete("/{id}", response_model=schemas.Speciality)
def delete_speciality(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a speciality.
    """
    speciality = crud.speciality.get(db=db, id=id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")
    speciality = crud.speciality.remove(db=db, id=id)
    return speciality
