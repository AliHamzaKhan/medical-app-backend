from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class AIReport(Base):
    __tablename__ = "ai_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text, nullable=True)
    report_type = Column(String, index=True)
    diagnosis = Column(Text, nullable=True)
    treatment = Column(Text, nullable=True)
    recommended_specialities = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="ai_reports")
    images = relationship("AIReportImage", back_populates="report")

class AIReportImage(Base):
    __tablename__ = "ai_report_images"

    id = Column(Integer, primary_key=True, index=True)
    ai_report_id = Column(Integer, ForeignKey("ai_reports.id"))
    image_path = Column(String, nullable=False)
    
    report = relationship("AIReport", back_populates="images")
