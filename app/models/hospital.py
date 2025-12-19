from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Hospital(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    pincode = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    contact_number = Column(String)
    email = Column(String)
    website = Column(String)
    description = Column(Text)

    # Other relationships can be added here, e.g., doctors, departments
