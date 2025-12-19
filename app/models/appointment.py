import enum
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class AppointmentStatus(str, enum.Enum):
    scheduled = "scheduled"
    completed = "completed"
    canceled = "canceled"
    no_show = "no_show"

class Appointment(Base):
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('users.id'))
    patient_id = Column(Integer, ForeignKey('users.id'))
    availability_id = Column(Integer, ForeignKey('availabilities.id'))
    appointment_time = Column(DateTime)
    status = Column(Enum(AppointmentStatus))
    details = Column(String)

    doctor = relationship('User', foreign_keys=[doctor_id])
    patient = relationship('User', foreign_keys=[patient_id])
    availability = relationship('Availability')
