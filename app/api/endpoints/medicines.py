from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post(
    "/",
    response_model=schemas.Medicine,
)
def create_medicine(
    *,
    db: Session = Depends(deps.get_db),
    medicine_in: schemas.MedicineCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new medicine.
    """
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    return medicine


@router.get("/", response_model=List[schemas.Medicine])
def read_medicines(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    q: Optional[str] = None,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve medicines.
    """
    if q:
        search_in = schemas.MedicineSearchHistoryCreate(search_query=q, user_id=current_user.id)
        crud.medicine_search_history.create(db=db, obj_in=search_in)
        db.commit()
    medicines = crud.medicine.get_multi(db, skip=skip, limit=limit)
    return medicines


@router.get("/{id}", response_model=schemas.Medicine)
def read_medicine(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get medicine by ID.
    """
    medicine = crud.medicine.get(db=db, id=id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine
