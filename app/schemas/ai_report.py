from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
import enum

class AIReportType(str, enum.Enum):
    SKIN = "skin"
    GENERAL = "general"

class AIReportImageBase(BaseModel):
    image_path: str

class AIReportImageCreate(AIReportImageBase):
    pass

class AIReportImage(AIReportImageBase):
    id: int
    ai_report_id: int

    model_config = ConfigDict(from_attributes=True)

class AIReportBase(BaseModel):
    description: Optional[str] = None
    report_type: AIReportType

class AIReportCreate(AIReportBase):
    user_id: int
    images: List[AIReportImageCreate]

class AIReportUpdate(AIReportBase):
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    doctors_recommended: Optional[List[str]] = None
    suggestions: Optional[List[str]] = None

class AIReport(AIReportBase):
    id: int
    user_id: int
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    doctors_recommended: Optional[str] = None
    suggestions: Optional[str] = None
    created_at: datetime
    images: List[AIReportImage] = []

    model_config = ConfigDict(from_attributes=True)
