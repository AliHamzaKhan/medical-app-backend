from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.patient import Patient, PatientCreate
from app.crud.patient import get_patient, get_patients, create_patient

router = APIRouter()

@router.post("/", response_model=Patient)
def create_new_patient(patient: PatientCreate, db: Session = Depends(deps.get_db)):
    return create_patient(db=db, patient=patient)

@router.get("/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, db: Session = Depends(deps.get_db)):
    db_patient = get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.get("/", response_model=list[Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    patients = get_patients(db, skip=skip, limit=limit)
    return patients
