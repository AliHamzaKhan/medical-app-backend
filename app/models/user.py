from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.doctor_speciality import doctor_speciality

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    role_id = Column(Integer, ForeignKey("role.id"))
    role = relationship("Role", back_populates="users")
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Patient Information
    phone = Column(String, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    allergic_reaction = Column(String, nullable=True)

    # Doctor Information
    specialities = relationship(
        "Speciality", secondary=doctor_speciality, back_populates="doctors"
    )
    documents = relationship("DoctorDocument", back_populates="owner")
    clinics = relationship("Clinic", back_populates="owner")

    subscriptions = relationship("Subscription", back_populates="user")
    ai_reports = relationship("AIReport", back_populates="user")
    total_ai_credits = Column(Integer, nullable=False, default=10)
    used_ai_credits = Column(Integer, nullable=False, default=0)

    total_medicine_search_credits = Column(Integer, nullable=False, default=50)
    used_medicine_search_credits = Column(Integer, nullable=False, default=0)

    medicine_search_history = relationship("MedicineSearchHistory", back_populates="user")

    @property
    def remaining_ai_credits(self):
        return self.total_ai_credits - self.used_ai_credits
    
    @property
    def remaining_medicine_search_credits(self):
        return self.total_medicine_search_credits - self.used_medicine_search_credits
