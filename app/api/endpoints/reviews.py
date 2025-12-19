from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.review import Review, ReviewCreate
from app.crud.review import get_review, get_reviews, create_review

router = APIRouter()

@router.post("/", response_model=Review)
def create_new_review(review: ReviewCreate, db: Session = Depends(deps.get_db)):
    return create_review(db=db, review=review)

@router.get("/{review_id}", response_model=Review)
def read_review(review_id: int, db: Session = Depends(deps.get_db)):
    db_review = get_review(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.get("/", response_model=list[Review])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    reviews = get_reviews(db, skip=skip, limit=limit)
    return reviews
