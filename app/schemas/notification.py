from pydantic import BaseModel
from datetime import datetime
from .user import User

class NotificationBase(BaseModel):
    title: str
    message: str
    status: str

class NotificationCreate(NotificationBase):
    user_id: int

class Notification(NotificationBase):
    id: int
    created_at: datetime
    user: User

    class Config:
        orm_mode = True
