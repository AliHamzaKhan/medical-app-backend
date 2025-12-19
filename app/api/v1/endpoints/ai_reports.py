from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional, Any
from app import crud, models, schemas
from app.api import deps
import shutil

router = APIRouter()

@router.post("/", response_model=schemas.AIReport)
def create_ai_report(
    *, 
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    images: List[UploadFile] = File(...),
    description: Optional[str] = Form(None),
    report_type: str = Form(...)
):
    """
    Create new AI report.
    """
    if current_user.remaining_ai_credits <= 0:
        raise HTTPException(status_code=403, detail="Not enough AI report credits")

    # 1. Save uploaded images to a temporary location
    image_paths = []
    for image in images:
        image_path = f"/tmp/{image.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_paths.append(image_path)

    # 2. Perform AI search (placeholder)
    diagnosis = "Sample Diagnosis"
    treatment = "Sample Treatment"
    recommended_specialities = "General Physician"

    # 3. Create AIReport object in database
    ai_report_in = schemas.AIReportCreate(
        user_id=current_user.id,
        description=description,
        report_type=report_type,
        images=[schemas.AIReportImageCreate(image_path=path) for path in image_paths]
    )
    ai_report = crud.ai_report.create_with_images(db=db, obj_in=ai_report_in)
    
    # Update the AI-generated fields
    ai_report.diagnosis = diagnosis
    ai_report.treatment = treatment
    ai_report.recommended_specialities = recommended_specialities
    db.add(ai_report)
    db.commit()
    db.refresh(ai_report)

    # 4. Decrement user's AI report credits
    current_user.used_ai_credits += 1
    db.add(current_user)
    db.commit()

    return ai_report

@router.get("/{report_id}", response_model=schemas.AIReport)
def read_ai_report(
    *, 
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    report_id: int
) -> Any:
    """
    Get AI report by ID.
    """
    ai_report = crud.ai_report.get(db=db, id=report_id)
    if not ai_report:
        raise HTTPException(status_code=404, detail="AI Report not found")
    if ai_report.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return ai_report

@router.get("/", response_model=List[schemas.AIReport])
def read_ai_reports(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve user's AI reports.
    """
    ai_reports = crud.ai_report.get_multi_by_user(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )
    return ai_reports
