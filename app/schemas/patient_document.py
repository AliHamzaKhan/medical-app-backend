from pydantic import BaseModel

class PatientDocumentBase(BaseModel):
    document_path: str | None = None

class PatientDocumentCreate(PatientDocumentBase):
    document_path: str

class PatientDocumentUpdate(PatientDocumentBase):
    pass

class PatientDocumentInDBBase(PatientDocumentBase):
    id: int
    document_path: str
    owner_id: int

    class Config:
        from_attributes = True

class PatientDocument(PatientDocumentInDBBase):
    pass

class PatientDocumentInDB(PatientDocumentInDBBase):
    pass
