
from fastapi import APIRouter

from app.api.v1.endpoints import (
    users, login, hospitals, patients, doctors, roles, 
    plans, subscriptions, ai_reports, packages, credits, profiles, specialities,
    clinics, doctor_documents, availability, appointments, medicines, data_process,
    medical_histories, medicine_search_histories, messages, notifications, payments,
    prescriptions, reviews
)

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(specialities.router, prefix="/specialities", tags=["specialities"])
api_router.include_router(hospitals.router, prefix="/hospitals", tags=["hospitals"])
api_router.include_router(patients.router, prefix="/patients", tags=["patients"])
api_router.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
api_router.include_router(plans.router, prefix="/plans", tags=["plans"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
api_router.include_router(ai_reports.router, prefix="/ai-reports", tags=["ai-reports"])
api_router.include_router(packages.router, prefix="/packages", tags=["packages"])
api_router.include_router(credits.router, prefix="/credits", tags=["credits"])
api_router.include_router(clinics.router, prefix="/clinics", tags=["clinics"])
api_router.include_router(doctor_documents.router, prefix="/doctor-documents", tags=["doctor-documents"])
api_router.include_router(availability.router, prefix="/availability", tags=["availability"])
api_router.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
api_router.include_router(medicines.router, prefix="/medicines", tags=["medicines"])
api_router.include_router(data_process.data_process_router, prefix="/data-process", tags=["data-process"])
api_router.include_router(medical_histories.router, prefix="/medical-histories", tags=["medical-histories"])
api_router.include_router(medicine_search_histories.router, prefix="/medicine-search-histories", tags=["medicine-search-histories"])
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
api_router.include_router(prescriptions.router, prefix="/prescriptions", tags=["prescriptions"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
