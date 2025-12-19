from app.crud.base import CRUDBase
from app.models.availability import Availability
from app.schemas.availability import AvailabilityCreate, AvailabilityUpdate

class CRUDAvailability(CRUDBase[Availability, AvailabilityCreate, AvailabilityUpdate]):
    def update(self, db, *, db_obj, obj_in):
        db_obj.is_booked = obj_in.is_booked
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

availability = CRUDAvailability(Availability)
