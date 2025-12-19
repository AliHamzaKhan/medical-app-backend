from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.appointment import Appointment, AppointmentStatus
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate

class CRUDAppointment(CRUDBase[Appointment, AppointmentCreate, AppointmentUpdate]):
    def get_appointments_by_doctor_and_time(
        self, db: Session, *, doctor_id: int, start_time: datetime, end_time: datetime
    ) -> List[Appointment]:
        return (
            db.query(self.model)
            .filter(
                self.model.doctor_id == doctor_id,
                self.model.start_time < end_time,
                self.model.end_time > start_time,
                self.model.status == AppointmentStatus.BOOKED,
            )
            .all()
        )
    
    def update(self, db: Session, *, db_obj: Appointment, obj_in: AppointmentUpdate) -> Appointment:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

appointment = CRUDAppointment(Appointment)
