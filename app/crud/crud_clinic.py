from app.crud.base import CRUDBase
from app.models.clinic import Clinic
from app.schemas.clinic import ClinicCreate, ClinicUpdate
from sqlalchemy.orm import Session


class CRUDClinic(CRUDBase[Clinic, ClinicCreate, ClinicUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ClinicCreate, owner_id: int
    ) -> Clinic:
        obj_in_data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


clinic = CRUDClinic(Clinic)
