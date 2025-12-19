from app.crud.base import CRUDBase
from app.models.medicine_search_history import MedicineSearchHistory
from app.schemas.user import MedicineSearchHistoryCreate

class CRUDMedicineSearchHistory(CRUDBase[MedicineSearchHistory, MedicineSearchHistoryCreate, MedicineSearchHistoryCreate]):
    pass

medicine_search_history = CRUDMedicineSearchHistory(MedicineSearchHistory)
