from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    departments = Column(String, nullable=True)
    website = Column(String, nullable=True)
    phone_no = Column(String, nullable=True)
    current_status = Column(String, nullable=True)
    image = Column(String, nullable=True)
    timings = Column(String, nullable=True)
