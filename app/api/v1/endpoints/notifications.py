from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Notification])
def read_notifications(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve notifications.
    """
    if crud.user.is_superuser(current_user):
        notifications = crud.notification.get_multi(db, skip=skip, limit=limit)
    else:
        notifications = crud.notification.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return notifications


@router.post("/", response_model=schemas.Notification)
def create_notification(
    *,
    db: Session = Depends(deps.get_db),
    notification_in: schemas.NotificationCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new notification.
    """
    notification = crud.notification.create_with_owner(db=db, obj_in=notification_in, owner_id=current_user.id)
    return notification


@router.get("/{id}", response_model=schemas.Notification)
def read_notification(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get notification by ID.
    """
    notification = crud.notification.get(db=db, id=id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    if not crud.user.is_superuser(current_user) and (notification.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return notification
