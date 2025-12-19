from app.crud.base import CRUDBase
from app.models.speciality import Speciality
from app.schemas.speciality import SpecialityCreate, SpecialityUpdate


class CRUDSpeciality(CRUDBase[Speciality, SpecialityCreate, SpecialityUpdate]):
    pass


speciality = CRUDSpeciality(Speciality)
