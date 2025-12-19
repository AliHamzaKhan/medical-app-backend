from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base

doctor_patient = Table(
    "doctor_patient",
    Base.metadata,
    Column("doctor_id", Integer, ForeignKey("doctor.id"), primary_key=True),
    Column("patient_id", Integer, ForeignKey("patient.id"), primary_key=True),
)

class Doctor(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String)
    hospital_id = Column(Integer, ForeignKey("hospital.id"))
    hospital = relationship("Hospital", back_populates="doctors")
    patients = relationship(
        "Patient", secondary=doctor_patient, back_populates="doctors"
    )
    availabilities = relationship("Availability", back_populates="doctor")
