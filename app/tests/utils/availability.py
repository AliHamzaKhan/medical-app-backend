
from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.availability import AvailabilityCreate
from app.tests.utils.hospital import create_random_hospital
from app.tests.utils.speciality import create_random_speciality

def create_random_availability(db: Session) -> models.Availability:
    hospital = create_random_hospital(db)
    speciality = create_random_speciality(db)
    availability_in = AvailabilityCreate(hospital_id=hospital.id, speciality_id=speciality.id, available_beds=10)
    return crud.availability.create(db=db, obj_in=availability_in)
