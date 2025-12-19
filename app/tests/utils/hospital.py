
from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.hospital import HospitalCreate
from app.tests.utils.utils import random_lower_string, random_float

def create_random_hospital(db: Session) -> models.Hospital:
    name = random_lower_string()
    address = random_lower_string()
    latitude = random_float()
    longitude = random_float()
    hospital_in = HospitalCreate(name=name, address=address, latitude=latitude, longitude=longitude)
    return crud.hospital.create(db=db, obj_in=hospital_in)
