from app.crud.base import CRUDBase
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorStatusUpdate
from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from datetime import date, datetime, time
from typing import List

class CRUDDoctor(CRUDBase[Doctor, DoctorCreate, DoctorUpdate]):
    def update_status(self, db: Session, *, db_obj: Doctor, obj_in: DoctorStatusUpdate) -> Doctor:
        db_obj.status = obj_in.status
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_doctor_schedule_today(self, db: Session, *, doctor_id: int) -> List[Appointment]:
        today = date.today()
        start_of_day = datetime.combine(today, time.min)
        end_of_day = datetime.combine(today, time.max)
        return db.query(Appointment).filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_time >= start_of_day,
            Appointment.appointment_time <= end_of_day
        ).all()

doctor = CRUDDoctor(Doctor)
