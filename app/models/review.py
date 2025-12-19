from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import datetime

class Review(Base):
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    rating = Column(Integer)
    comment = Column(Text)
    review_date = Column(DateTime, default=datetime.datetime.utcnow)

    doctor = relationship('Doctor')
    patient = relationship('Patient')
