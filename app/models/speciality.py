from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base

class Speciality(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    doctors = relationship(
        "Doctor", secondary="doctor_speciality", back_populates="specialities"
    )
