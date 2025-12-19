from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.DoctorDocument])
def read_doctor_documents(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve doctor documents.
    """
    if crud.user.is_superuser(current_user):
        doctor_documents = crud.doctor_document.get_multi(db, skip=skip, limit=limit)
    else:
        doctor_documents = crud.doctor_document.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return doctor_documents


@router.post("/", response_model=schemas.DoctorDocument)
def create_doctor_document(
    *, 
    db: Session = Depends(deps.get_db),
    doctor_document_in: schemas.DoctorDocumentCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new doctor document.
    """
    doctor_document = crud.doctor_document.create_with_owner(db=db, obj_in=doctor_document_in, owner_id=current_user.id)
    return doctor_document


@router.put("/{id}", response_model=schemas.DoctorDocument)
def update_doctor_document(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    doctor_document_in: schemas.DoctorDocumentUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a doctor document.
    """
    doctor_document = crud.doctor_document.get(db=db, id=id)
    if not doctor_document:
        raise HTTPException(status_code=404, detail="Doctor document not found")
    if not crud.user.is_superuser(current_user) and (doctor_document.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    doctor_document = crud.doctor_document.update(db=db, db_obj=doctor_document, obj_in=doctor_document_in)
    return doctor_document


@router.get("/{id}", response_model=schemas.DoctorDocument)
def read_doctor_document(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get doctor document by ID.
    """
    doctor_document = crud.doctor_document.get(db=db, id=id)
    if not doctor_document:
        raise HTTPException(status_code=404, detail="Doctor document not found")
    if not crud.user.is_superuser(current_user) and (doctor_document.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return doctor_document


@router.delete("/{id}", response_model=schemas.DoctorDocument)
def delete_doctor_document(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a doctor document.
    """
    doctor_document = crud.doctor_document.get(db=db, id=id)
    if not doctor_document:
        raise HTTPException(status_code=404, detail="Doctor document not found")
    if not crud.user.is_superuser(current_user) and (doctor_document.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    doctor_document = crud.doctor_document.remove(db=db, id=id)
    return doctor_document
