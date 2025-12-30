from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import crud, models, schemas
from ... import deps

router = APIRouter()


@router.post("/", response_model=schemas.Patient)
def create_patient(
    *, 
    db: Session = Depends(deps.get_db), 
    patient_in: schemas.PatientCreate,
) -> Any:
    """
    Create new patient.
    """
    patient = crud.patient.create(db, obj_in=patient_in)
    return patient


@router.get("/", response_model=List[schemas.Patient])
def read_patients(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve patients.
    """
    patients = crud.patient.get_multi(db, skip=skip, limit=limit)
    return patients

@router.get("/{patient_id}", response_model=schemas.Patient)
def read_patient(
    *, 
    db: Session = Depends(deps.get_db), 
    patient_id: int,
) -> Any:
    """
    Get patient by ID.
    """
    patient = crud.patient.get(db, id=patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.put("/{patient_id}", response_model=schemas.Patient)
def update_patient(
    *, 
    db: Session = Depends(deps.get_db), 
    patient_id: int, 
    patient_in: schemas.PatientUpdate,
) -> Any:
    """
    Update a patient.
    """
    patient = crud.patient.get(db, id=patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient = crud.patient.update(db, db_obj=patient, obj_in=patient_in)
    return patient


@router.delete("/{patient_id}", response_model=schemas.Patient)
def delete_patient(
    *, 
    db: Session = Depends(deps.get_db), 
    patient_id: int,
) -> Any:
    """
    Delete a patient.
    """
    patient = crud.patient.get(db, id=patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient = crud.patient.remove(db, id=patient_id)
    return patient
