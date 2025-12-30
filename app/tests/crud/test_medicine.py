from sqlalchemy.orm import Session

from app import crud
from app.schemas.medicine import MedicineCreate, MedicineUpdate
from app.tests.utils.utils import random_lower_string

def test_create_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    manufacturer = random_lower_string()
    dosage = random_lower_string()
    price = 10.0
    medicine_in = MedicineCreate(name=name, description=description, manufacturer=manufacturer, dosage=dosage, price=price)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    assert medicine.name == name
    assert medicine.description == description
    assert medicine.manufacturer == manufacturer
    assert medicine.dosage == dosage
    assert medicine.price == price

def test_get_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    manufacturer = random_lower_string()
    dosage = random_lower_string()
    price = 10.0
    medicine_in = MedicineCreate(name=name, description=description, manufacturer=manufacturer, dosage=dosage, price=price)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    stored_medicine = crud.medicine.get(db=db, id=medicine.id)
    assert stored_medicine
    assert medicine.id == stored_medicine.id
    assert medicine.name == stored_medicine.name

def test_update_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    manufacturer = random_lower_string()
    dosage = random_lower_string()
    price = 10.0
    medicine_in = MedicineCreate(name=name, description=description, manufacturer=manufacturer, dosage=dosage, price=price)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    description2 = random_lower_string()
    medicine_update = MedicineUpdate(description=description2)
    medicine2 = crud.medicine.update(db=db, db_obj=medicine, obj_in=medicine_update)
    assert medicine.id == medicine2.id
    assert medicine.name == medicine2.name
    assert medicine2.description == description2

def test_delete_medicine(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    manufacturer = random_lower_string()
    dosage = random_lower_string()
    price = 10.0
    medicine_in = MedicineCreate(name=name, description=description, manufacturer=manufacturer, dosage=dosage, price=price)
    medicine = crud.medicine.create(db=db, obj_in=medicine_in)
    medicine2 = crud.medicine.remove(db=db, id=medicine.id)
    medicine3 = crud.medicine.get(db=db, id=medicine.id)
    assert medicine3 is None
    assert medicine2.id == medicine.id
    assert medicine2.name == name
