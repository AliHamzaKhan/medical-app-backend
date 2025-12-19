from sqlalchemy import Column, Integer, String, Float
from app.db.base_class import Base

class Package(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    credits_granted = Column(Integer)
    role = Column(String) # "doctor" or "patient"
