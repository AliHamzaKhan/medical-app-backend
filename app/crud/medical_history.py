from sqlalchemy.orm import Session
from app.models.medical_history import MedicalHistory
from app.schemas.medical_history import MedicalHistoryCreate

def get_medical_history(db: Session, medical_history_id: int):
    return db.query(MedicalHistory).filter(MedicalHistory.id == medical_history_id).first()

def get_medical_histories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MedicalHistory).offset(skip).limit(limit).all()

def create_medical_history(db: Session, medical_history: MedicalHistoryCreate):
    db_medical_history = MedicalHistory(**medical_history.dict())
    db.add(db_medical_history)
    db.commit()
    db.refresh(db_medical_history)
    return db_medical_history
