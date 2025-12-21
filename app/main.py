from fastapi import FastAPI
from app.api.api import api_router
from app.db.session import SessionLocal
from app.db.base import Base
from app.db.session import engine

# Import all models here to ensure they are registered with SQLAlchemy
from app.models.ai_report import AIReport
from app.models.appointment import Appointment
from app.models.availability import Availability
from app.models.clinic import Clinic
from app.models.doctor import Doctor
from app.models.doctor_document import DoctorDocument
from app.models.hospital import Hospital
from app.models.medical_history import MedicalHistory
from app.models.medicine import Medicine
from app.models.medicine_search_history import MedicineSearchHistory
from app.models.message import Message
from app.models.notification import Notification
from app.models.package import Package
from app.models.patient import Patient
from app.models.payment import Payment
from app.models.plan import Plan
from app.models.prescription import Prescription
from app.models.review import Review
from app.models.role import Role
from app.models.speciality import Speciality
from app.models.subscription import Subscription
from app.models.user import User

from app.db.initial_data import pre_populate_specialities

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        pre_populate_specialities(db)
    finally:
        db.close()
