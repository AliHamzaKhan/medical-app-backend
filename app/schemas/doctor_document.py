from pydantic import BaseModel


class DoctorDocumentBase(BaseModel):
    document_path: str | None = None


class DoctorDocumentCreate(DoctorDocumentBase):
    document_path: str


class DoctorDocumentUpdate(DoctorDocumentBase):
    pass


class DoctorDocumentInDBBase(DoctorDocumentBase):
    id: int
    document_path: str
    owner_id: int

    class Config:
        orm_mode = True


class DoctorDocument(DoctorDocumentInDBBase):
    pass


class DoctorDocumentInDB(DoctorDocumentInDBBase):
    pass
