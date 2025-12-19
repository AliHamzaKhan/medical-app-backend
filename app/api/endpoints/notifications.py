from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.notification import Notification, NotificationCreate
from app.crud.notification import get_notification, get_notifications, create_notification

router = APIRouter()

@router.post("/", response_model=Notification)
def create_new_notification(notification: NotificationCreate, db: Session = Depends(deps.get_db)):
    return create_notification(db=db, notification=notification)

@router.get("/{notification_id}", response_model=Notification)
def read_notification(notification_id: int, db: Session = Depends(deps.get_db)):
    db_notification = get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification

@router.get("/", response_model=list[Notification])
def read_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    notifications = get_notifications(db, skip=skip, limit=limit)
    return notifications
