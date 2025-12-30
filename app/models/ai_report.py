from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.schemas.ai_report import AIReportType


class AIReport(Base):
    __tablename__ = "ai_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(String)
    report_type = Column(SQLAlchemyEnum(AIReportType), nullable=False)
    diagnosis = Column(String, nullable=True)
    treatment = Column(String, nullable=True)
    doctors_recommended = Column(String, nullable=True)
    suggestions = Column(String, nullable=True)

    user = relationship("User", back_populates="ai_reports")
    images = relationship("AIReportImage", back_populates="report", cascade="all, delete-orphan")
