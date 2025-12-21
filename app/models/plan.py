from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    features = Column(String)
