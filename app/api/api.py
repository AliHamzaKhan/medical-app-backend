from fastapi import APIRouter
from app.api.endpoints import (login, users, roles, specialities, hospitals, clinics, availabilities, doctors, patients, appointments, prescriptions, medical_histories, messages, notifications, payments, reviews, medicines, packages, plans)

api_router = APIRouter()

endpoint_modules = [
    (login, "login", "Login"),
    (users, "users", "Users"),
    (roles, "roles", "Roles"),
    (specialities, "specialities", "Specialities"),
    (hospitals, "hospitals", "Hospitals"),
    (clinics, "clinics", "Clinics"),
    (availabilities, "availabilities", "Availabilities"),
    (doctors, "doctors", "Doctors"),
    (patients, "patients", "Patients"),
    (appointments, "appointments", "Appointments"),
    (prescriptions, "prescriptions", "Prescriptions"),
    (medical_histories, "medical_histories", "Medical Histories"),
    (messages, "messages", "Messages"),
    (notifications, "notifications", "Notifications"),
    (payments, "payments", "Payments"),
    (reviews, "reviews", "Reviews"),
    (medicines, "medicines", "Medicines"),
    (packages, "packages", "Packages"),
    (plans, "plans", "Plans"),
]

for module, prefix, tag in endpoint_modules:
    api_router.include_router(module.router, prefix=f"/{prefix}", tags=[tag])
