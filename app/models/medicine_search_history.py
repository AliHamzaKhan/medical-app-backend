from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class MedicineSearchHistory(Base):
    __tablename__ = "medicine_search_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="medicine_search_history")
    search_query = Column(String, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=True)
    medicine = relationship("Medicine")
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
