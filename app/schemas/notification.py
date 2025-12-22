from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Shared properties
class NotificationBase(BaseModel):
    message: Optional[str] = None
    is_read: Optional[int] = None
    timestamp: Optional[datetime] = None


# Properties to receive on item creation
class NotificationCreate(NotificationBase):
    user_id: int
    message: str


# Properties to receive on item update
class NotificationUpdate(NotificationBase):
    pass


# Properties shared by models in DB
class NotificationInDBBase(NotificationBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Notification(NotificationInDBBase):
    pass


# Properties properties stored in DB
class NotificationInDB(NotificationInDBBase):
    pass
