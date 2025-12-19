import enum
from sqlalchemy import Column, Integer, String, Boolean, Date, Enum as EnumDB, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class UserRole(str, enum.Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    address = Column(String)
    role = Column(EnumDB(UserRole))

    clinics = relationship("Clinic", back_populates="owner")
    doctor_profile = relationship('Doctor', uselist=False, back_populates='user')
    patient_profile = relationship('Patient', uselist=False, back_populates='user')
    medical_histories = relationship('MedicalHistory', back_populates='user')
    notifications = relationship('Notification', back_populates='user')
