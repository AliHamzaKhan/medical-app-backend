
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Clinic)
def create_clinic(
    *, 
    db: Session = Depends(deps.get_db), 
    clinic_in: schemas.ClinicCreate, 
    current_user: models.User = Depends(deps.get_current_active_user)
) -> schemas.Clinic:
    return crud.clinic.create_with_owner(db=db, obj_in=clinic_in, owner_id=current_user.id)


@router.get("/{clinic_id}", response_model=schemas.Clinic)
def read_clinic(clinic_id: int, db: Session = Depends(deps.get_db)):
    db_clinic = crud.clinic.get(db=db, id=clinic_id)
    if db_clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return db_clinic


@router.get("/", response_model=list[schemas.Clinic])
def read_clinics(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    clinics = crud.clinic.get_multi(db=db, skip=skip, limit=limit)
    return clinics


@router.put("/{clinic_id}", response_model=schemas.Clinic)
def update_clinic(clinic_id: int, clinic: schemas.ClinicUpdate, db: Session = Depends(deps.get_db)):
    db_clinic = crud.clinic.get(db=db, id=clinic_id)
    if db_clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return crud.clinic.update(db=db, db_obj=db_clinic, obj_in=clinic)


@router.delete("/{clinic_id}", response_model=schemas.Clinic)
def delete_clinic(clinic_id: int, db: Session = Depends(deps.get_db)):
    db_clinic = crud.clinic.get(db=db, id=clinic_id)
    if db_clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return crud.clinic.remove(db=db, id=clinic_id)
