from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Speciality)
def create_speciality(speciality: schemas.SpecialityCreate, db: Session = Depends(get_db)):
    speciality = crud.speciality.create(db=db, obj_in=speciality)
    db.commit()
    db.refresh(speciality)
    return speciality

@router.get("/{speciality_id}", response_model=schemas.Speciality)
def read_speciality(speciality_id: int, db: Session = Depends(get_db)):
    db_speciality = crud.speciality.get(db=db, id=speciality_id)
    if db_speciality is None:
        raise HTTPException(status_code=404, detail="Speciality not found")
    return db_speciality

@router.get("/", response_model=list[schemas.Speciality])
def read_specialities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    specialities = crud.speciality.get_multi(db=db, skip=skip, limit=limit)
    return specialities

@router.put("/{speciality_id}", response_model=schemas.Speciality)
def update_speciality(speciality_id: int, speciality: schemas.SpecialityUpdate, db: Session = Depends(get_db)):
    db_speciality = crud.speciality.get(db=db, id=speciality_id)
    if db_speciality is None:
        raise HTTPException(status_code=404, detail="Speciality not found")
    speciality = crud.speciality.update(db=db, db_obj=db_speciality, obj_in=speciality)
    db.commit()
    db.refresh(speciality)
    return speciality

@router.delete("/{speciality_id}", response_model=schemas.Speciality)
def delete_speciality(speciality_id: int, db: Session = Depends(get_db)):
    db_speciality = crud.speciality.get(db=db, id=speciality_id)
    if db_speciality is None:
        raise HTTPException(status_code=404, detail="Speciality not found")
    speciality = crud.speciality.remove(db=db, id=speciality_id)
    db.commit()
    return speciality
