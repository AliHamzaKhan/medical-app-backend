from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from app.db.base import Base

doctor_speciality = Table(
    "doctor_speciality",
    Base.metadata,
    Column("doctor_id", Integer, ForeignKey("doctors.id")),
    Column("speciality_id", Integer, ForeignKey("specialities.id")),
)

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    years_of_experience = Column(Integer)
    consultation_fee = Column(Float)
    bio = Column(String)

    user = relationship("User")
    specialities = relationship("Speciality", secondary=doctor_speciality, back_populates="doctors")
