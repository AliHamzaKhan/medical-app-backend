from sqlalchemy import Column, Integer, String, Boolean, Date, Enum as EnumDB, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class UserRole(str, enum.Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

doctor_speciality = Table(
    'doctor_speciality',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('speciality_id', Integer, ForeignKey('specialities.id'), primary_key=True)
)

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

    doctor_profile = relationship('Doctor', uselist=False, back_populates='user')
    patient_profile = relationship('Patient', uselist=False, back_populates='user')
    medical_histories = relationship('MedicalHistory', back_populates='user')
    notifications = relationship('Notification', back_populates='user')
    specialities = relationship('Speciality', secondary=doctor_speciality, back_populates='users')
