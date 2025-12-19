
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Doctor(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    experience_years = Column(Integer)
    consultation_fee = Column(Integer)
    bio = Column(Text)
    
    user = relationship('User', back_populates='doctor_profile')
    documents = relationship('DoctorDocument', back_populates='doctor')
