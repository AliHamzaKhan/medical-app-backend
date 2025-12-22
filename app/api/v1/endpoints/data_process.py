from typing import Any, Optional, List

from fastapi import APIRouter, Depends, Body, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.gemini import MyGemini
from app.core.prompts import DataProcessPrompts
from app.core.s3 import AmazonS3Bucket
from app.schemas.ai_report import AIReportType, AIReportUpdate
from PIL import Image

data_process_router = APIRouter()


@data_process_router.post('/process_data')
async def process_data(report_id: int = Body(...),
                       db: Session = Depends(deps.get_db)
                       ) -> Any:
    """
    Process an AI report.
    """
    report = crud.ai_report.get(db, id=report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    if not report.images:
        raise HTTPException(status_code=400, detail="Report has no images")

    image_path = report.images[0].image_path
    # This is a placeholder for reading the image from the path
    # You should replace this with your actual implementation
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Image not found at path: {image_path}")

    # Process the image with AI
    gemini = MyGemini()
    prompt = DataProcessPrompts(report.report_type)
    ai_generated_text, token_used = await gemini.generate_ai(ai_request_type=report.report_type, image=img)

    # This is a placeholder for parsing the AI generated text
    # You should replace this with your actual implementation
    try:
        ai_data = schemas.AiGeneratedText.parse_raw(ai_generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing AI generated text: {e}")

    report_update = AIReportUpdate(
        diagnosis=ai_data.diagnosis,
        treatment=ai_data.treatment,
        doctors_recommended=ai_data.doctors_recommended,
        suggestions=ai_data.suggestions
    )

    updated_report = crud.ai_report.update(db, db_obj=report, obj_in=report_update)

    return updated_report


@data_process_router.post('/get_process_data')
def get_process_data(report_id: int = Body(...),
                       db: Session = Depends(deps.get_db)
                       ) -> Any:
    """
    Get the processed data for an AI report.
    """
    report = crud.ai_report.get(db, id=report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    return report


@data_process_router.post('/add_data_process')
async def add_data_process(user_id: int = Body(...),
                           description: str = Body(...),
                           report_type: AIReportType = Body(...),
                           file: UploadFile = File(...),
                           db: Session = Depends(deps.get_db)
                           ) -> Any:
    """
    Create a new AI report and process the data.
    """
    image_url = await AmazonS3Bucket().upload_file_to_folder(file=file, folder_name='ai_process_images')

    image_create = schemas.AIReportImageCreate(image_path=image_url.get('file_url'))

    report_create = schemas.AIReportCreate(
        user_id=user_id,
        description=description,
        report_type=report_type,
        images=[image_create]
    )

    report = crud.ai_report.create_with_images(db, obj_in=report_create)

    return await process_data(report_id=report.id, db=db)


@data_process_router.post('/update_data_process')
async def update_data_process(report_id: int = Body(...),
                              file: UploadFile = File(...),
                              db: Session = Depends(deps.get_db)
                              ) -> Any:
    """
    Update an existing AI report with a new image and reprocess the data.
    """
    report = crud.ai_report.get(db, id=report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    image_url = await AmazonS3Bucket().upload_file_to_folder(file=file, folder_name='ai_process_images')

    # This assumes we are replacing all existing images with the new one
    for image in report.images:
        db.delete(image)

    db_image = models.AIReportImage(
        ai_report_id=report.id,
        image_path=image_url.get('file_url')
    )
    db.add(db_image)
    db.commit()
    db.refresh(report)

    return await process_data(report_id=report.id, db=db)
