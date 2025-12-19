from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    formula = Column(String, nullable=False)
    side_effects = Column(Text, nullable=True)
    used_for = Column(Text, nullable=True)
    dosage_usage = Column(Text, nullable=True)
    alternatives = Column(Text, nullable=True)  # For doctors
    dose_calculator_info = Column(Text, nullable=True)  # For doctors