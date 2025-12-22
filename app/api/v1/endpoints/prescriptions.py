from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Prescription])
def read_prescriptions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve prescriptions.
    """
    if crud.user.is_superuser(current_user):
        prescriptions = crud.prescription.get_multi(db, skip=skip, limit=limit)
    else:
        prescriptions = crud.prescription.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return prescriptions


@router.post("/", response_model=schemas.Prescription)
def create_prescription(
    *,
    db: Session = Depends(deps.get_db),
    prescription_in: schemas.PrescriptionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new prescription.
    """
    prescription = crud.prescription.create_with_owner(db=db, obj_in=prescription_in, owner_id=current_user.id)
    return prescription


@router.get("/{id}", response_model=schemas.Prescription)
def read_prescription(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get prescription by ID.
    """
    prescription = crud.prescription.get(db=db, id=id)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    if not crud.user.is_superuser(current_user) and (prescription.appointment.patient_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return prescription
