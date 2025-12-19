from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.crud import crud_subscription

router = APIRouter()


@router.post("/", response_model=schemas.Subscription)
def create_subscription(
    *, 
    db: Session = Depends(deps.get_db),
    subscription_in: schemas.SubscriptionCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new subscription.
    """
    subscription = crud_subscription.create_subscription(db=db, subscription_in=subscription_in)
    return subscription


@router.get("/", response_model=List[schemas.Subscription])
def read_subscriptions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve subscriptions.
    """
    if crud.user.is_superuser(current_user):
        subscriptions = crud_subscription.get_subscriptions(db, skip=skip, limit=limit)
    else:
        subscriptions = crud_subscription.get_subscriptions_by_user(db, user_id=current_user.id)
    return subscriptions
