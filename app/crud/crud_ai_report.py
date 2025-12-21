from typing import List
from app.crud.base import CRUDBase
from app.models.ai_report import AIReport
from app.models.ai_report_image import AIReportImage
from app.schemas.ai_report import AIReportCreate, AIReportUpdate, AIReportImageCreate
from sqlalchemy.orm import Session

class CRUDAIReport(CRUDBase[AIReport, AIReportCreate, AIReportUpdate]):
    def create_with_images(self, db: Session, *, obj_in: AIReportCreate) -> AIReport:
        db_obj = AIReport(
            user_id=obj_in.user_id,
            description=obj_in.description,
            report_type=obj_in.report_type
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        for image in obj_in.images:
            db_image = AIReportImage(
                ai_report_id=db_obj.id,
                image_path=image.image_path
            )
            db.add(db_image)
        
        db.commit()
        db.refresh(db_obj)

        return db_obj

ai_report = CRUDAIReport(AIReport)
