from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.MedicineSearchHistory])
def read_medicine_search_histories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve medicine search histories.
    """
    if crud.user.is_superuser(current_user):
        medicine_search_histories = crud.medicine_search_history.get_multi(db, skip=skip, limit=limit)
    else:
        medicine_search_histories = crud.medicine_search_history.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return medicine_search_histories


@router.post("/", response_model=schemas.MedicineSearchHistory)
def create_medicine_search_history(
    *,
    db: Session = Depends(deps.get_db),
    medicine_search_history_in: schemas.MedicineSearchHistoryCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new medicine search history.
    """
    medicine_search_history = crud.medicine_search_history.create_with_owner(db=db, obj_in=medicine_search_history_in, owner_id=current_user.id)
    return medicine_search_history


@router.get("/{id}", response_model=schemas.MedicineSearchHistory)
def read_medicine_search_history(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get medicine search history by ID.
    """
    medicine_search_history = crud.medicine_search_history.get(db=db, id=id)
    if not medicine_search_history:
        raise HTTPException(status_code=404, detail="Medicine search history not found")
    if not crud.user.is_superuser(current_user) and (medicine_search_history.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return medicine_search_history
