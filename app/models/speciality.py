from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.doctor import doctor_speciality

class Speciality(Base):
    __tablename__ = 'specialities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    doctors = relationship(
        "Doctor", secondary=doctor_speciality, back_populates="specialities"
    )
