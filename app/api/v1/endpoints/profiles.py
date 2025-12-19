from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.storage import get_storage_client

router = APIRouter()


@router.post("/specialities", response_model=schemas.Speciality)
def add_speciality_to_doctor(
    *, 
    db: Session = Depends(deps.get_db),
    speciality_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Add a speciality to the current doctor's profile.
    """
    if not crud.user.is_doctor(current_user):
        raise HTTPException(status_code=403, detail="Not a doctor")
    speciality = crud.speciality.get(db=db, id=speciality_id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")
    if speciality in current_user.specialities:
        raise HTTPException(status_code=400, detail="Speciality already added")
    crud.user.add_speciality(db=db, user=current_user, speciality=speciality)
    return speciality

@router.delete("/specialities/{id}", response_model=schemas.Speciality)
def remove_speciality_from_doctor(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Remove a speciality from the current doctor's profile.
    """
    if not crud.user.is_doctor(current_user):
        raise HTTPException(status_code=403, detail="Not a doctor")
    speciality = crud.speciality.get(db=db, id=id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")
    if speciality not in current_user.specialities:
        raise HTTPException(status_code=400, detail="Speciality not in profile")
    crud.user.remove_speciality(db=db, user=current_user, speciality=speciality)
    return speciality

@router.post("/documents", response_model=schemas.DoctorDocument)
def upload_document(
    *, 
    db: Session = Depends(deps.get_db),
    file: UploadFile = File(...),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Upload a document for the current doctor.
    """
    if not crud.user.is_doctor(current_user):
        raise HTTPException(status_code=403, detail="Not a doctor")

    storage_client = get_storage_client()
    file_path = storage_client.upload_file(file.file, file.filename)

    document_in = schemas.DoctorDocumentCreate(document_path=file_path)
    document = crud.doctor_document.create_with_owner(
        db=db, obj_in=document_in, owner_id=current_user.id
    )
    return document


@router.delete("/documents/{id}", response_model=schemas.DoctorDocument)
def delete_document(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Delete a document for the current doctor.
    """
    document = crud.doctor_document.get(db=db, id=id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    if document.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not the owner")
    
    storage_client = get_storage_client()
    storage_client.delete_file(document.document_path)

    crud.doctor_document.remove(db=db, id=id)
    return document


@router.post("/clinics", response_model=schemas.Clinic)
def create_clinic(
    *, 
    db: Session = Depends(deps.get_db),
    clinic_in: schemas.ClinicCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create a new clinic for the current doctor.
    """
    if not crud.user.is_doctor(current_user):
        raise HTTPException(status_code=403, detail="Not a doctor")
    clinic = crud.clinic.create_with_owner(db=db, obj_in=clinic_in, owner_id=current_user.id)
    return clinic


@router.put("/clinics/{id}", response_model=schemas.Clinic)
def update_clinic(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    clinic_in: schemas.ClinicUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update a clinic for the current doctor.
    """
    clinic = crud.clinic.get(db=db, id=id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    if clinic.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not the owner")
    clinic = crud.clinic.update(db=db, db_obj=clinic, obj_in=clinic_in)
    return clinic


@router.delete("/clinics/{id}", response_model=schemas.Clinic)
def delete_clinic(
    *, 
    db: Session = Depends(deps.get_DAb),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Delete a clinic for the current doctor.
    """
    clinic = crud.clinic.get(db=db, id=id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    if clinic.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not the owner")
    crud.clinic.remove(db=db, id=id)
    return clinic
