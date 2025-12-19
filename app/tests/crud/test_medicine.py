from sqlalchemy.orm import Session

from app import crud
from app.schemas.medicine import MedicineCreate, MedicineUpdate
from app.tests.utils.utils import random_lower_string


def test_create_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    medicine_in = MedicineCreate(name=name, description=description)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    assert medicine.name == name
    assert medicine.description == description


def test_get_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    medicine_in = MedicineCreate(name=name, description=description)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    stored_medicine = crud.medicine.get(db=db, id=medicine.id)
    assert stored_medicine
    assert stored_medicine.name == name
    assert stored_medicine.description == description


def test_update_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    medicine_in = MedicineCreate(name=name, description=description)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    description2 = random_lower_string()
    medicine_update = MedicineUpdate(description=description2)
    medicine2 = crud.medicine.update(db=db, db_obj=medicine, obj_in=medicine_update)
    assert medicine2.name == name
    assert medicine2.description == description2


def test_delete_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    medicine_in = MedicineCreate(name=name, description=description)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    medicine2 = crud.medicine.remove(db=db, id=medicine.id)
    medicine3 = crud.medicine.get(db=db, id=medicine.id)
    assert medicine3 is None
    assert medicine2.id == medicine.id
    assert medicine2.name == name
    assert medicine2.description == description
