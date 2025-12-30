from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import crud
from ... import deps
from ....schemas.hospital import Hospital, HospitalUpdate

router = APIRouter()


@router.get("/", response_model=List[Hospital])
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


@router.put("/{hospital_id}", response_model=Hospital)
def update_hospital(
    *,
    db: Session = Depends(deps.get_db),
    hospital_id: int,
    hospital_in: HospitalUpdate,
) -> Any:
    """
    Update a hospital.
    """
    hospital = crud.hospital.get(db, id=hospital_id)
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    hospital = crud.hospital.update(db, db_obj=hospital, obj_in=hospital_in)
    return hospital


@router.get("/{hospital_id}", response_model=Hospital)
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


@router.delete("/{hospital_id}", response_model=Hospital)
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
