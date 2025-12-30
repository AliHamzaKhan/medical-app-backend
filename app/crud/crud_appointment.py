from typing import List

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate


class CRUDAppointment(CRUDBase[Appointment, AppointmentCreate, AppointmentUpdate]):
    def get_multi_by_doctor(
        self, db: Session, *, doctor_id: int, start_time: str, end_time: str
    ) -> List[Appointment]:
        return (
            db.query(self.model)
            .filter(
                self.model.doctor_id == doctor_id,
                self.model.appointment_time >= start_time,
                self.model.appointment_time <= end_time,
            )
            .all()
        )


appointment = CRUDAppointment(Appointment)
