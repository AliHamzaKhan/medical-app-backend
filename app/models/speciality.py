from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.doctor_speciality import doctor_speciality


class Speciality(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    doctors = relationship(
        "User", secondary=doctor_speciality, back_populates="specialities"
    )
