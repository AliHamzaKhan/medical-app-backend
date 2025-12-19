from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.appointment import Appointment, AppointmentCreate
from app.crud.appointment import get_appointment, get_appointments, create_appointment, update_appointment, delete_appointment

router = APIRouter()

@router.post("/", response_model=Appointment)
def create_new_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db=db, appointment=appointment)

@router.get("/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = get_appointment(db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.get("/", response_model=list[Appointment])
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = get_appointments(db, skip=skip, limit=limit)
    return appointments

@router.put("/{appointment_id}", response_model=Appointment)
def update_existing_appointment(appointment_id: int, appointment: AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = update_appointment(db, appointment_id=appointment_id, appointment=appointment)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.delete("/{appointment_id}", response_model=Appointment)
def delete_existing_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = delete_appointment(db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment
