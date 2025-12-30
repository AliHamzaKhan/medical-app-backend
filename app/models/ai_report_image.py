from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class AIReportImage(Base):
    __tablename__ = "ai_report_images"

    id = Column(Integer, primary_key=True, index=True)
    ai_report_id = Column(Integer, ForeignKey("ai_reports.id"), nullable=False)
    image_path = Column(String, nullable=False)

    report = relationship("AIReport", back_populates="images")
