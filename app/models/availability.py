import enum
from sqlalchemy import Column, Integer, Time, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship
from app.db.base import Base

class AvailabilityStatus(str, enum.Enum):
    available = "available"
    booked = "booked"
    unavailable = "unavailable"

class Availability(Base):
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    status = Column(Enum(AvailabilityStatus))

    doctor = relationship('User', back_populates='availabilities')
