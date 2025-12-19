from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Clinic])
def read_clinics(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve clinics.
    """
    if crud.user.is_superuser(current_user):
        clinics = crud.clinic.get_multi(db, skip=skip, limit=limit)
    else:
        clinics = crud.clinic.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return clinics


@router.post("/", response_model=schemas.Clinic)
def create_clinic(
    *, 
    db: Session = Depends(deps.get_db),
    clinic_in: schemas.ClinicCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new clinic.
    """
    clinic = crud.clinic.create_with_owner(db=db, obj_in=clinic_in, owner_id=current_user.id)
    return clinic


@router.put("/{id}", response_model=schemas.Clinic)
def update_clinic(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    clinic_in: schemas.ClinicUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a clinic.
    """
    clinic = crud.clinic.get(db=db, id=id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    if not crud.user.is_superuser(current_user) and (clinic.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    clinic = crud.clinic.update(db=db, db_obj=clinic, obj_in=clinic_in)
    return clinic


@router.get("/{id}", response_model=schemas.Clinic)
def read_clinic(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get clinic by ID.
    """
    clinic = crud.clinic.get(db=db, id=id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    if not crud.user.is_superuser(current_user) and (clinic.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return clinic


@router.delete("/{id}", response_model=schemas.Clinic)
def delete_clinic(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a clinic.
    """
    clinic = crud.clinic.get(db=db, id=id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    if not crud.user.is_superuser(current_user) and (clinic.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    clinic = crud.clinic.remove(db=db, id=id)
    return clinic
