import enum
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class AppointmentStatus(str, enum.Enum):
    BOOKED = "booked"
    CANCELLED = "cancelled"

class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    patient_id = Column(Integer, ForeignKey("patient.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(Enum(AppointmentStatus), nullable=False, default=AppointmentStatus.BOOKED)
    doctor = relationship("Doctor")
    patient = relationship("Patient")
