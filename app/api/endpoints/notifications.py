from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.notification import Notification, NotificationCreate
from app.crud import notification

router = APIRouter()

@router.post("/", response_model=Notification)
def create_new_notification(notification_in: NotificationCreate, db: Session = Depends(deps.get_db)):
    return notification.create(db=db, obj_in=notification_in)

@router.get("/{notification_id}", response_model=Notification)
def read_notification(notification_id: int, db: Session = Depends(deps.get_db)):
    db_notification = notification.get(db, id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification

@router.get("/", response_model=list[Notification])
def read_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    notifications = notification.get_multi(db, skip=skip, limit=limit)
    return notifications
