from sqlalchemy import Column, Integer, String, Float
from app.db.base_class import Base

class Hospital(Base):
    __tablename__ = "hospitals"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    departments = Column(String, nullable=True)
    website = Column(String, nullable=True)
    phone_no = Column(String, nullable=True)
    current_status = Column(String, nullable=True)
    image = Column(String, nullable=True)
    timings = Column(String, nullable=True)
