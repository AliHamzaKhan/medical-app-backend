from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.MedicalHistory])
def read_medical_histories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve medical histories.
    """
    if crud.user.is_superuser(current_user):
        medical_histories = crud.medical_history.get_multi(db, skip=skip, limit=limit)
    else:
        medical_histories = crud.medical_history.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return medical_histories


@router.post("/", response_model=schemas.MedicalHistory)
def create_medical_history(
    *,
    db: Session = Depends(deps.get_db),
    medical_history_in: schemas.MedicalHistoryCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new medical history.
    """
    medical_history = crud.medical_history.create_with_owner(db=db, obj_in=medical_history_in, owner_id=current_user.id)
    return medical_history


@router.put("/{id}", response_model=schemas.MedicalHistory)
def update_medical_history(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    medical_history_in: schemas.MedicalHistoryUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a medical history.
    """
    medical_history = crud.medical_history.get(db=db, id=id)
    if not medical_history:
        raise HTTPException(status_code=404, detail="Medical history not found")
    if not crud.user.is_superuser(current_user) and (medical_history.patient_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    medical_history = crud.medical_history.update(db=db, db_obj=medical_history, obj_in=medical_history_in)
    return medical_history


@router.get("/{id}", response_model=schemas.MedicalHistory)
def read_medical_history(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get medical history by ID.
    """
    medical_history = crud.medical_history.get(db=db, id=id)
    if not medical_history:
        raise HTTPException(status_code=404, detail="Medical history not found")
    if not crud.user.is_superuser(current_user) and (medical_history.patient_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return medical_history


@router.delete("/{id}", response_model=schemas.MedicalHistory)
def delete_medical_history(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a medical history.
    """
    medical_history = crud.medical_history.get(db=db, id=id)
    if not medical_history:
        raise HTTPException(status_code=404, detail="Medical history not found")
    if not crud.user.is_superuser(current_user) and (medical_history.patient_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    medical_history = crud.medical_history.remove(db=db, id=id)
    return medical_history
