from typing import Any, List
import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Hospital)
def create_hospital(
    *, 
    db: Session = Depends(deps.get_db), 
    hospital_in: schemas.HospitalCreate,
) -> Any:
    """
    Create new hospital.
    """
    hospital = crud.hospital.create(db, obj_in=hospital_in)
    return hospital


@router.post("/upload-excel", response_model=List[schemas.Hospital])
def create_hospitals_from_excel(
    *, 
    db: Session = Depends(deps.get_db),
    file: UploadFile = File(...),
) -> Any:
    """
    Create new hospitals from an Excel file.
    """
    try:
        df = pd.read_excel(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading Excel file: {e}")

    hospitals = []
    for _, row in df.iterrows():
        hospital_in = schemas.HospitalCreate(
            name=row["Name"],
            departments=row.get("Departments"),
            address=row.get("Address"),
            website=row.get("Website"),
            phone_no=row.get("PhoneNo"),
            current_status=row.get("CurrentStatus"),
            image=row.get("Image"),
            timings=row.get("Timings"),
            latitude=row.get("Latitude"),
            longitude=row.get("Longitude"),
        )
        hospital = crud.hospital.create(db, obj_in=hospital_in)
        hospitals.append(hospital)
    
    return hospitals


@router.get("/", response_model=List[schemas.Hospital])
def read_hospitals(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve hospitals.
    """
    hospitals = crud.hospital.get_multi(db, skip=skip, limit=limit)
    return hospitals

@router.get("/{hospital_id}", response_model=schemas.Hospital)
def read_hospital(
    *, 
    db: Session = Depends(deps.get_db), 
    hospital_id: int,
) -> Any:
    """
    Get hospital by ID.
    """
    hospital = crud.hospital.get(db, id=hospital_id)
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital


@router.put("/{hospital_id}", response_model=schemas.Hospital)
def update_hospital(
    *, 
    db: Session = Depends(deps.get_db), 
    hospital_id: int, 
    hospital_in: schemas.HospitalUpdate,
) -> Any:
    """
    Update a hospital.
    """
    hospital = crud.hospital.get(db, id=hospital_id)
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    hospital = crud.hospital.update(db, db_obj=hospital, obj_in=hospital_in)
    return hospital


@router.delete("/{hospital_id}", response_model=schemas.Hospital)
def delete_hospital(
    *, 
    db: Session = Depends(deps.get_db), 
    hospital_id: int,
) -> Any:
    """
    Delete a hospital.
    """
    hospital = crud.hospital.get(db, id=hospital_id)
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    hospital = crud.hospital.remove(db, id=hospital_id)
    return hospital
