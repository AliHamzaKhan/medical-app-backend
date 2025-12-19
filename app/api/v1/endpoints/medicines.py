from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.medicine import Medicine, MedicineForDoctor
from app.schemas.user import MedicineSearchHistoryCreate
import datetime

router = APIRouter()

@router.get("/", response_model=List[Medicine])
def search_medicines(
    q: str,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Search for medicines (for patients).
    """
    if current_user.remaining_medicine_search_credits <= 0:
        raise HTTPException(status_code=403, detail="Not enough credits")

    medicines = db.query(crud.medicine.model).filter(
        crud.medicine.model.name.ilike(f"%{q}% ") |
        crud.medicine.model.formula.ilike(f"%{q}%")
    ).all()

    current_user.used_medicine_search_credits += 1
    for medicine in medicines:
        history_entry = MedicineSearchHistoryCreate(search_query=q, timestamp=datetime.datetime.utcnow(), user_id=current_user.id, medicine_id=medicine.id)
        crud.medicine_search_history.create(db, obj_in=history_entry)
    db.commit()

    return medicines

@router.get("/doctor/", response_model=List[MedicineForDoctor])
def search_medicines_for_doctor(
    q: str,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_doctor),
) -> Any:
    """
    Search for medicines (for doctors).
    """
    if current_user.remaining_medicine_search_credits <= 0:
        raise HTTPException(status_code=403, detail="Not enough credits")

    medicines = db.query(crud.medicine.model).filter(
        crud.medicine.model.name.ilike(f"%{q}%") |
        crud.medicine.model.formula.ilike(f"%{q}%")
    ).all()

    current_user.used_medicine_search_credits += 1
    for medicine in medicines:
        history_entry = MedicineSearchHistoryCreate(search_query=q, timestamp=datetime.datetime.utcnow(), user_id=current_user.id, medicine_id=medicine.id)
        crud.medicine_search_history.create(db, obj_in=history_entry)
    db.commit()

    return medicines
