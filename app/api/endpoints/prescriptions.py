from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.prescription import Prescription, PrescriptionCreate
from app.crud.prescription import get_prescription, get_prescriptions, create_prescription

router = APIRouter()

@router.post("/", response_model=Prescription)
def create_new_prescription(prescription: PrescriptionCreate, db: Session = Depends(deps.get_db)):
    return create_prescription(db=db, prescription=prescription)

@router.get("/{prescription_id}", response_model=Prescription)
def read_prescription(prescription_id: int, db: Session = Depends(deps.get_db)):
    db_prescription = get_prescription(db, prescription_id=prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription

@router.get("/", response_model=list[Prescription])
def read_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    prescriptions = get_prescriptions(db, skip=skip, limit=limit)
    return prescriptions
