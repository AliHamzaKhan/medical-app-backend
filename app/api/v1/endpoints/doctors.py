from fastapi import APIRouter, Depends, Query, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import shutil

from app import crud, models
from app.api import deps
from app.schemas.doctor import Doctor, DoctorCreate, DoctorStatusUpdate
from app.schemas.doctor_document import DoctorDocumentCreate
from app.schemas.user import User

router = APIRouter()


@router.post("/", response_model=Doctor)
def create_doctor(
    *, 
    db: Session = Depends(deps.get_db),
    doctor_in: DoctorCreate,
    documents: List[UploadFile] = File(...),
    current_user: models.User = Depends(deps.get_current_active_user)
):
    """
    Create a new doctor.
    """
    doctor = crud.doctor.create(db, obj_in=doctor_in)
    for document in documents:
        file_path = f"uploads/{document.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(document.file, buffer)
        crud.doctor_document.create(db, obj_in=DoctorDocumentCreate(doctor_id=doctor.id, document_type=document.content_type, document_url=file_path))
    return doctor

@router.put("/{doctor_id}/status", response_model=Doctor)
def update_doctor_status(
    *, 
    db: Session = Depends(deps.get_db),
    doctor_id: int,
    status_in: DoctorStatusUpdate,
    current_user: models.User = Depends(deps.get_current_active_user) # Add admin check here
):
    """
    Update a doctor's status.
    """
    doctor = crud.doctor.get(db, id=doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctor = crud.doctor.update_status(db, db_obj=doctor, obj_in=status_in)
    return doctor

@router.get("/me", response_model=Doctor)
def read_doctor_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
):
    """
    Get current doctor's status.
    """
    doctor = crud.doctor.get(db, id=current_user.id) # This assumes user id and doctor id are the same, which might need adjustment
    return doctor

@router.get("/", response_model=List[Doctor])
def read_doctors(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user) # Add admin check here
):
    """
    Retrieve doctors.
    """
    doctors = crud.doctor.get_multi(db, skip=skip, limit=limit)
    return doctors

@router.get("/search/", response_model=List[User])
def search_doctors(
    db: Session = Depends(deps.get_db),
    latitude: Optional[float] = Query(None),
    longitude: Optional[float] = Query(None),
    radius: Optional[float] = Query(None, description="Search radius in kilometers"),
    speciality: Optional[str] = Query(None),
    hospital: Optional[str] = Query(None),
    name: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 100,
) -> List[models.User]:
    """
    Search for doctors with various filters.
    """
    doctors = crud.user.search_doctors(
        db,
        latitude=latitude,
        longitude=longitude,
        radius=radius,
        speciality=speciality,
        hospital=hospital,
        name=name,
        skip=skip,
        limit=limit,
    )
    return doctors
