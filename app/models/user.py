
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    role_id = Column(Integer, ForeignKey("role.id"))
    role = relationship("Role", back_populates="users")
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    specialization = Column(String, nullable=True)
