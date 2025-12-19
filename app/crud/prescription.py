from sqlalchemy.orm import Session
from app.models.prescription import Prescription
from app.schemas.prescription import PrescriptionCreate

def get_prescription(db: Session, prescription_id: int):
    return db.query(Prescription).filter(Prescription.id == prescription_id).first()

def get_prescriptions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Prescription).offset(skip).limit(limit).all()

def create_prescription(db: Session, prescription: PrescriptionCreate):
    db_prescription = Prescription(**prescription.dict())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription
