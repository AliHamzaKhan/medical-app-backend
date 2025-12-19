from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.doctor import doctor_patient


class Patient(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(Date)
    address = Column(String)
    hospital_id = Column(Integer, ForeignKey("hospital.id"))
    hospital = relationship("Hospital", back_populates="patients")
    doctors = relationship("Doctor", secondary=doctor_patient, back_populates="patients")
