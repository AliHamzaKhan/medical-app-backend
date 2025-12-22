from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.appointment import Appointment, AppointmentCreate
from app.crud.crud_appointment import appointment

router = APIRouter()

@router.post("/", response_model=Appointment)
def create_new_appointment(appointment_in: AppointmentCreate, db: Session = Depends(deps.get_db)):
    return appointment.create(db=db, obj_in=appointment_in)

@router.get("/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: int, db: Session = Depends(deps.get_db)):
    db_appointment = appointment.get(db, id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.get("/", response_model=list[Appointment])
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    appointments = appointment.get_multi(db, skip=skip, limit=limit)
    return appointments

@router.put("/{appointment_id}", response_model=Appointment)
def update_existing_appointment(appointment_id: int, appointment_in: AppointmentCreate, db: Session = Depends(deps.get_db)):
    db_appointment = appointment.update(db, db_obj=appointment.get(db, id=appointment_id), obj_in=appointment_in)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.delete("/{appointment_id}", response_model=Appointment)
def delete_existing_appointment(appointment_id: int, db: Session = Depends(deps.get_db)):
    db_appointment = appointment.remove(db, id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment
