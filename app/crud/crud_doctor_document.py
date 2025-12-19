from app.crud.base import CRUDBase
from app.models.doctor_document import DoctorDocument
from app.schemas.doctor_document import DoctorDocumentCreate, DoctorDocumentUpdate


class CRUDDoctorDocument(CRUDBase[DoctorDocument, DoctorDocumentCreate, DoctorDocumentUpdate]):
    pass


doctor_document = CRUDDoctorDocument(DoctorDocument)
