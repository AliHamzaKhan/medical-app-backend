from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import datetime

class MedicineSearchHistory(Base):
    __tablename__ = "medicine_search_histories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    search_query = Column(String)
    search_timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User")
