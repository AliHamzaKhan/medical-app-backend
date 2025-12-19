from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class DoctorDocument(Base):
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    document_type = Column(String)  # e.g., 'license', 'degree'
    document_path = Column(String)
    is_verified = Column(String, default=False)

    doctor = relationship('Doctor', back_populates='documents')
