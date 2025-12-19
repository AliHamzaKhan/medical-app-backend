from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AIReportImageBase(BaseModel):
    image_path: str

class AIReportImageCreate(AIReportImageBase):
    pass

class AIReportImage(AIReportImageBase):
    id: int
    ai_report_id: int

    class Config:
        from_attributes = True

class AIReportBase(BaseModel):
    description: Optional[str] = None
    report_type: str

class AIReportCreate(AIReportBase):
    user_id: int
    images: List[AIReportImageCreate]

class AIReportUpdate(AIReportBase):
    pass

class AIReport(AIReportBase):
    id: int
    user_id: int
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    recommended_specialities: Optional[str] = None
    created_at: datetime
    images: List[AIReportImage] = []

    class Config:
        from_attributes = True
