from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
