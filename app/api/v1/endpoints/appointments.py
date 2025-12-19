
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from app.models.appointment import AppointmentStatus

router = APIRouter()


@router.post("/", response_model=schemas.Appointment)
def create_appointment(
    *, 
    db: Session = Depends(deps.get_db),
    appointment_in: schemas.AppointmentCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new appointment.
    """
    # Check for overlapping appointments
    overlapping_appointments = crud.appointment.get_appointments_by_doctor_and_time(
        db=db,
        doctor_id=appointment_in.doctor_id,
        start_time=appointment_in.start_time,
        end_time=appointment_in.end_time,
    )
    if overlapping_appointments:
        raise HTTPException(
            status_code=409,
            detail="An appointment with this doctor already exists during the requested time.",
        )

    # Get the availability and check if it's already booked
    availability = crud.availability.get(db=db, id=appointment_in.availability_id)
    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found")
    if availability.is_booked:
        raise HTTPException(status_code=400, detail="This availability is already booked")

    # Create the appointment
    appointment = crud.appointment.create(db=db, obj_in=appointment_in)

    # Update the availability to mark it as booked
    availability_update = schemas.AvailabilityUpdate(is_booked=True)
    crud.availability.update(db=db, db_obj=availability, obj_in=availability_update)

    return appointment


@router.get("/", response_model=List[schemas.Appointment])
def read_appointments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Retrieve appointments.
    """
    appointments = crud.appointment.get_multi(db, skip=skip, limit=limit)
    return appointments


@router.get("/{id}", response_model=schemas.Appointment)
def read_appointment(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get appointment by ID.
    """
    appointment = crud.appointment.get(db=db, id=id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


@router.put("/{id}", response_model=schemas.Appointment)
def update_appointment(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    appointment_in: schemas.AppointmentUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update an appointment.
    """
    appointment = crud.appointment.get(db=db, id=id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    # If the appointment is being canceled, free up the availability
    if appointment_in.status == AppointmentStatus.CANCELLED and appointment.status != AppointmentStatus.CANCELLED:
        availability = crud.availability.get(db=db, id=appointment.availability_id)
        if availability:
            availability_update = schemas.AvailabilityUpdate(is_booked=False)
            crud.availability.update(db=db, db_obj=availability, obj_in=availability_update)

    appointment = crud.appointment.update(db=db, db_obj=appointment, obj_in=appointment_in)
    return appointment


@router.delete("/{id}", response_model=schemas.Appointment)
def delete_appointment(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Delete an appointment.
    """
    appointment = crud.appointment.get(db=db, id=id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    # Free up the availability
    availability = crud.availability.get(db=db, id=appointment.availability_id)
    if availability:
        availability_update = schemas.AvailabilityUpdate(is_booked=False)
        crud.availability.update(db=db, db_obj=availability, obj_in=availability_update)
        
    appointment = crud.appointment.remove(db=db, id=id)
    return appointment
