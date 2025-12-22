import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum, Date
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.core.security import get_password_hash, verify_password

class UserRole(str, enum.Enum):
    PATIENT = "patient"
    DOCTOR = "doctor"
    SUPERUSER = "superuser"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    role = Column(Enum(UserRole))
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    address = Column(String)
    remaining_medicine_search_credits = Column(Integer, default=0)

    ai_reports = relationship("AIReport", back_populates="user")

    def set_password(self, password):
        self.hashed_password = get_password_hash(password)

    def check_password(self, password):
        return verify_password(password, self.hashed_password)
