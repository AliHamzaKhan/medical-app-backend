from app.crud.base import CRUDBase
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorStatusUpdate
from sqlalchemy.orm import Session

class CRUDDoctor(CRUDBase[Doctor, DoctorCreate, DoctorUpdate]):
    def update_status(self, db: Session, *, db_obj: Doctor, obj_in: DoctorStatusUpdate) -> Doctor:
        db_obj.status = obj_in.status
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

doctor = CRUDDoctor(Doctor)
