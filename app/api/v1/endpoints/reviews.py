from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Review])
def read_reviews(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve reviews.
    """
    if crud.user.is_superuser(current_user):
        reviews = crud.review.get_multi(db, skip=skip, limit=limit)
    else:
        reviews = crud.review.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return reviews


@router.post("/", response_model=schemas.Review)
def create_review(
    *,
    db: Session = Depends(deps.get_db),
    review_in: schemas.ReviewCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new review.
    """
    review = crud.review.create_with_owner(db=db, obj_in=review_in, owner_id=current_user.id)
    return review


@router.get("/{id}", response_model=schemas.Review)
def read_review(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get review by ID.
    """
    review = crud.review.get(db=db, id=id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    if not crud.user.is_superuser(current_user) and (review.patient_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return review
