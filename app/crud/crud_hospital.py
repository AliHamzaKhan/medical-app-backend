from app.crud.base import CRUDBase
from app.models.hospital import Hospital
from app.schemas.hospital import HospitalCreate, HospitalUpdate

class CRUDHospital(CRUDBase[Hospital, HospitalCreate, HospitalUpdate]):
    def create(self, db, *, obj_in):
        db_obj = Hospital(
            name=obj_in.name,
            address=obj_in.address,
            latitude=obj_in.latitude,
            longitude=obj_in.longitude,
            phone_no=obj_in.phone_no,
            website=obj_in.website,
            timings=obj_in.timings,
            departments=obj_in.departments,
            image=obj_in.image,
            current_status=obj_in.current_status,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

hospital = CRUDHospital(Hospital)
