from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Availability)
def create_availability(availability: schemas.AvailabilityCreate, db: Session = Depends(get_db)):
    return crud.availability.create(db=db, obj_in=availability)

@router.get("/{availability_id}", response_model=schemas.Availability)
def read_availability(availability_id: int, db: Session = Depends(get_db)):
    db_availability = crud.availability.get(db=db, id=availability_id)
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    return db_availability

@router.get("/", response_model=list[schemas.Availability])
def read_availabilities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    availabilities = crud.availability.get_multi(db=db, skip=skip, limit=limit)
    return availabilities

@router.put("/{availability_id}", response_model=schemas.Availability)
def update_availability(availability_id: int, availability: schemas.AvailabilityUpdate, db: Session = Depends(get_db)):
    db_availability = crud.availability.get(db=db, id=availability_id)
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    return crud.availability.update(db=db, db_obj=db_availability, obj_in=availability)

@router.delete("/{availability_id}", response_model=schemas.Availability)
def delete_availability(availability_id: int, db: Session = Depends(get_db)):
    db_availability = crud.availability.get(db=db, id=availability_id)
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    return crud.availability.remove(db=db, id=availability_id)
