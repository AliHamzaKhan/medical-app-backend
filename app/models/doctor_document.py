from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class DoctorDocument(Base):
    __tablename__ = "doctor_documents"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    document_type = Column(String)
    document_url = Column(String)

    doctor = relationship("Doctor")
