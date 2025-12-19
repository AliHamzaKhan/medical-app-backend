from sqlalchemy.orm import Session
from app.models.speciality import Speciality

def pre_populate_specialities(db: Session):
    specialities = [
        "Cardiology", "Dermatology", "Endocrinology", "Gastroenterology",
        "Neurology", "Oncology", "Ophthalmology", "Orthopedics",
        "Otolaryngology", "Pediatrics", "Psychiatry", "Pulmonology",
        "Radiology", "Urology", "Anesthesiology", "General Surgery",
        "Internal Medicine", "Family Medicine", "Emergency Medicine",
        "Obstetrics and Gynecology", "Pathology", "Physical Medicine and Rehabilitation",
        "Allergy and Immunology", "Nephrology", "Rheumatology", "Infectious Disease",
        "Hematology", "Geriatrics", "Neonatology", "Sports Medicine"
    ]
    for speciality_name in specialities:
        speciality = db.query(Speciality).filter(Speciality.name == speciality_name).first()
        if not speciality:
            db_speciality = Speciality(name=speciality_name)
            db.add(db_speciality)
    db.commit()
