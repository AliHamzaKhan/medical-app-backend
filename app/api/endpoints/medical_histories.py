from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.medical_history import MedicalHistory, MedicalHistoryCreate
from app.crud.crud_medical_history import medical_history

router = APIRouter()

@router.post("/", response_model=MedicalHistory)
def create_new_medical_history(medical_history_in: MedicalHistoryCreate, db: Session = Depends(deps.get_db)):
    return medical_history.create(db=db, obj_in=medical_history_in)

@router.get("/{medical_history_id}", response_model=MedicalHistory)
def read_medical_history(medical_history_id: int, db: Session = Depends(deps.get_db)):
    db_medical_history = medical_history.get(db, id=medical_history_id)
    if db_medical_history is None:
        raise HTTPException(status_code=404, detail="Medical history not found")
    return db_medical_history

@router.get("/", response_model=list[MedicalHistory])
def read_medical_histories(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    medical_histories = medical_history.get_multi(db, skip=skip, limit=limit)
    return medical_histories
