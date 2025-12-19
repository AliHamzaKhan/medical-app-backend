from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class AIReport(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(Text)
    report_type = Column(String)
    diagnosis = Column(Text)
    treatment = Column(Text)
    recommended_specialities = Column(String)  # Comma-separated
    created_at = Column(DateTime, server_default=func.now())

    user = relationship('User', back_populates='ai_reports')
    images = relationship('AIReportImage', back_populates='report')

class AIReportImage(Base):
    id = Column(Integer, primary_key=True, index=True)
    ai_report_id = Column(Integer, ForeignKey('ai_reports.id'))
    image_path = Column(String)

    report = relationship('AIReport', back_populates='images')
