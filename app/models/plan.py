from sqlalchemy import Column, Integer, String, Float

from app.db.base_class import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    duration_days = Column(Integer)
