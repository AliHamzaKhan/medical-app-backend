from app.crud.base import CRUDBase
from app.models.medical_history import MedicalHistory
from app.schemas.medical_history import MedicalHistoryCreate, MedicalHistoryUpdate

class CRUDMedicalHistory(CRUDBase[MedicalHistory, MedicalHistoryCreate, MedicalHistoryUpdate]):
    pass

medical_history = CRUDMedicalHistory(MedicalHistory)
