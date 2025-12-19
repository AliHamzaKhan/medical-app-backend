from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class MedicalHistory(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    condition_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    notes = Column(Text)

    user = relationship('User', back_populates='medical_histories')
