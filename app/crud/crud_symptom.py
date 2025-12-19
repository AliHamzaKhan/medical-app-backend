from app.crud.base import CRUDBase
from app.models.symptom import Symptom
from app.schemas.symptom import SymptomCreate, SymptomUpdate


class CRUDSymptom(CRUDBase[Symptom, SymptomCreate, SymptomUpdate]):
    pass


symptom = CRUDSymptom(Symptom)