import enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class NotificationStatus(str, enum.Enum):
    read = "read"
    unread = "unread"

class Notification(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum(NotificationStatus))

    user = relationship('User', back_populates='notifications')
