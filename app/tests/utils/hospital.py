
from sqlalchemy.orm import Session

from app import crud
from app.models.hospital import Hospital
from app.schemas.hospital import HospitalCreate
from app.tests.utils.utils import random_lower_string, random_float

def create_random_hospital(db: Session) -> Hospital:
    name = random_lower_string()
    address = random_lower_string()
    latitude = random_float(-90, 90)
    longitude = random_float(-180, 180)
    phone_no = "1234567890"
    website = "example.com"
    timings = "9am-5pm"
    current_status = "open"
    image = "image.png"
    hospital_in = HospitalCreate(name=name, address=address, latitude=latitude, longitude=longitude, phone_no=phone_no, website=website, timings=timings, current_status=current_status, image=image)
    return crud.hospital.create(db=db, obj_in=hospital_in)
