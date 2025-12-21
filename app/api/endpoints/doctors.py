from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.doctor import Doctor, DoctorCreate
from app.crud import doctor

router = APIRouter()

@router.post("/", response_model=Doctor)
def create_new_doctor(doctor_in: DoctorCreate, db: Session = Depends(deps.get_db)):
    return doctor.create(db=db, obj_in=doctor_in)

@router.get("/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(deps.get_db)):
    db_doctor = doctor.get(db, id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@router.get("/", response_model=list[Doctor])
def read_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    doctors = doctor.get_multi(db, skip=skip, limit=limit)
    return doctors
