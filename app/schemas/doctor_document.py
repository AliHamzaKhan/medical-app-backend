from pydantic import BaseModel, ConfigDict
from typing import Optional

class DoctorDocumentBase(BaseModel):
    doctor_id: int
    document_type: str
    document_url: str

class DoctorDocumentCreate(DoctorDocumentBase):
    pass

class DoctorDocumentUpdate(BaseModel):
    doctor_id: Optional[int] = None
    document_type: Optional[str] = None
    document_url: Optional[str] = None

class DoctorDocument(DoctorDocumentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
