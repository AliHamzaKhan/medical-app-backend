from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    manufacturer = Column(String)
    dosage = Column(String)
