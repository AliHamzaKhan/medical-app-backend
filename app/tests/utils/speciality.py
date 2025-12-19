
from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.speciality import SpecialityCreate
from app.tests.utils.utils import random_lower_string

def create_random_speciality(db: Session) -> models.Speciality:
    name = random_lower_string()
    speciality_in = SpecialityCreate(name=name)
    return crud.speciality.create(db=db, obj_in=speciality_in)
