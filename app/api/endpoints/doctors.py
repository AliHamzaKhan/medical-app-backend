from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.doctor import Doctor, DoctorCreate
from app.crud.doctor import get_doctor, get_doctors, create_doctor

router = APIRouter()

@router.post("/", response_model=Doctor)
def create_new_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    return create_doctor(db=db, doctor=doctor)

@router.get("/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = get_doctor(db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@router.get("/", response_model=list[Doctor])
def read_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doctors = get_doctors(db, skip=skip, limit=limit)
    return doctors
