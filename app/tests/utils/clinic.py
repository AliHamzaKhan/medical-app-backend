from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.models.clinic import Clinic
from app.schemas.clinic import ClinicCreate
from app.tests.utils.utils import random_lower_string


def create_random_clinic(db: Session, client: TestClient) -> Clinic:
    from app.tests.utils.user import create_random_user
    user, _ = create_random_user(db, client)
    clinic_name = random_lower_string()
    clinic_in = ClinicCreate(name=clinic_name, address=random_lower_string(), city=random_lower_string(),
                             phone_number=random_lower_string(10), owner_id=user.id)
    return crud.clinic.create(db=db, obj_in=clinic_in)
