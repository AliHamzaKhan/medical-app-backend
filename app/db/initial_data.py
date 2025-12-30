from sqlalchemy.orm import Session
from app.crud.crud_speciality import speciality
from app.schemas.speciality import SpecialityCreate

def pre_populate_specialities(db: Session):
    specialities = [
        "Cardiology",
        "Dermatology",
        "Neurology",
        "Pediatrics",
        "Orthopedics",
        "Gynecology",
        "Urology",
        "Oncology",
        "Psychiatry",
        "Endocrinology",
        "Gastroenterology",
        "Pulmonology",
        "Nephrology",
        "Rheumatology",
        "Hematology",
        "Ophthalmology",
        "Otolaryngology (ENT)",
        "General Surgery",
        "Plastic Surgery",
        "Neurosurgery",
        "Cardiothoracic Surgery",
        "Vascular Surgery",
        "Anesthesiology",
        "Radiology",
        "Pathology",
        "Emergency Medicine",
        "Family Medicine",
        "Internal Medicine",
        "Infectious Disease",
        "Allergy & Immunology",
        "Sports Medicine",
        "Physical Medicine & Rehabilitation",
        "Geriatrics",
        "Neonatology",
        "Pediatric Surgery",
        "Colorectal Surgery",
        "Bariatric Surgery",
        "Pain Management",
        "Sleep Medicine",
        "Nuclear Medicine",
        "Preventive Medicine",
        "Occupational Medicine",
        "Critical Care Medicine"]
    for spec in specialities:
        speciality_in_db = speciality.get_by_name(db, name=spec)
        if not speciality_in_db:
            speciality.create(db, obj_in=SpecialityCreate(name=spec))
