from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from app.db.base import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    
    doctor = relationship("User", back_populates="schedules")
    appointments = relationship("Appointment", back_populates="schedule")