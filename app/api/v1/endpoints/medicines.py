from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from app.models.user import User
from app.schemas.medicine import Medicine, MedicineCreate, MedicineUpdate
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
        crud.medicine.model.name.ilike(f"%{q}%")
    ).all()

    current_user.used_medicine_search_credits += 1
    for medicine in medicines:
        history_entry = MedicineSearchHistoryCreate(search_query=q, timestamp=datetime.datetime.utcnow(), user_id=current_user.id, medicine_id=medicine.id)
        crud.medicine_search_history.create(db, obj_in=history_entry)
    db.commit()

    return medicines

@router.post("/", response_model=Medicine)
def create_medicine(
    *,
    db: Session = Depends(deps.get_db),
    medicine_in: MedicineCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new medicine.
    """
    medicine = crud.medicine.create(db, obj_in=medicine_in)
    return medicine

@router.put("/{id}", response_model=Medicine)
def update_medicine(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    medicine_in: MedicineUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a medicine.
    """
    medicine = crud.medicine.get(db, id=id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    medicine = crud.medicine.update(db, db_obj=medicine, obj_in=medicine_in)
    return medicine

@router.get("/{id}", response_model=Medicine)
def read_medicine_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a specific medicine by id.
    """
    medicine = crud.medicine.get(db, id=id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine

@router.delete("/{id}", response_model=Medicine)
def delete_medicine(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a medicine.
    """
    medicine = crud.medicine.get(db, id=id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    medicine = crud.medicine.remove(db, id=id)
    return medicine
