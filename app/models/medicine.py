from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    description = Column(String, nullable=True)
