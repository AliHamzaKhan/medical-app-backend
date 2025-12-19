from app.crud.base import CRUDBase
from app.models.medicine import Medicine
from app.schemas.medicine import MedicineCreate, MedicineForDoctor

class CRUDMedicine(CRUDBase[Medicine, MedicineCreate, MedicineForDoctor]):
    pass

medicine = CRUDMedicine(Medicine)
