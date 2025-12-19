from sqlalchemy.orm import Session
import random
import string
from app import crud, models
from app.schemas.medicine import MedicineCreate

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def create_random_medicine(db: Session) -> models.Medicine:
    name = random_lower_string()
    medicine_in = MedicineCreate(name=name, description=random_lower_string())
    return crud.medicine.create(db=db, obj_in=medicine_in)
