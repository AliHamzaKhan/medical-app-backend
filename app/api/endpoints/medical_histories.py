from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.medical_history import MedicalHistory, MedicalHistoryCreate
from app.crud.medical_history import get_medical_history, get_medical_histories, create_medical_history

router = APIRouter()

@router.post("/", response_model=MedicalHistory)
def create_new_medical_history(medical_history: MedicalHistoryCreate, db: Session = Depends(get_db)):
    return create_medical_history(db=db, medical_history=medical_history)

@router.get("/{medical_history_id}", response_model=MedicalHistory)
def read_medical_history(medical_history_id: int, db: Session = Depends(get_db)):
    db_medical_history = get_medical_history(db, medical_history_id=medical_history_id)
    if db_medical_history is None:
        raise HTTPException(status_code=404, detail="Medical history not found")
    return db_medical_history

@router.get("/", response_model=list[MedicalHistory])
def read_medical_histories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medical_histories = get_medical_histories(db, skip=skip, limit=limit)
    return medical_histories
