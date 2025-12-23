from sqlalchemy.orm import Session
from app.crud.crud_speciality import speciality
from app.schemas.speciality import SpecialityCreate

def pre_populate_specialities(db: Session):
    specialities = [
        "Cardiology", "Dermatology", "Neurology", "Pediatrics", "Orthopedics",
        "Gynecology", "Urology", "Oncology", "Psychiatry", "Endocrinology"
    ]
    for spec in specialities:
        speciality_in_db = speciality.get_by_name(db, name=spec)
        if not speciality_in_db:
            speciality.create(db, obj_in=SpecialityCreate(name=spec))
