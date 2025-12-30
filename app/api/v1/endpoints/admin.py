from typing import Any, List
import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.hospital import Hospital, HospitalCreate
from app.schemas.doctor import Doctor, DoctorStatusUpdate
from app.models.doctor import DoctorStatus
from app.schemas.review import Review

router = APIRouter()


@router.post("/hospitals/", response_model=Hospital)
def create_hospital(
    *,
    db: Session = Depends(deps.get_db),
    hospital_in: HospitalCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new hospital.
    """
    hospital = crud.hospital.create(db, obj_in=hospital_in)
    return hospital


@router.post("/hospitals/upload-excel", response_model=List[Hospital])
def create_hospitals_from_excel(
    *,
    db: Session = Depends(deps.get_db),
    file: UploadFile = File(...),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new hospitals from an Excel file.
    """
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "text/csv"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an Excel or CSV file.")
    try:
        if file.content_type == "text/csv":
            df = pd.read_csv(file.file)
        else:
            df = pd.read_excel(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file: {e}")

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

@router.put("/doctors/{doctor_id}/approve", response_model=Doctor)
def approve_doctor(
    *,
    db: Session = Depends(deps.get_db),
    doctor_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Approve a doctor's profile.
    """
    doctor = crud.doctor.get(db, id=doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctor_update = DoctorStatusUpdate(status=DoctorStatus.approved)
    updated_doctor = crud.doctor.update_status(db, db_obj=doctor, obj_in=doctor_update)
    return updated_doctor


@router.put("/doctors/{doctor_id}/reject", response_model=Doctor)
def reject_doctor(
    *,
    db: Session = Depends(deps.get_db),
    doctor_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Reject a doctor's profile.
    """
    doctor = crud.doctor.get(db, id=doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctor_update = DoctorStatusUpdate(status=DoctorStatus.rejected)
    updated_doctor = crud.doctor.update_status(db, db_obj=doctor, obj_in=doctor_update)
    return updated_doctor


@router.put("/users/{user_id}/block", response_model=schemas.User)
def block_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Block a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_update = schemas.UserUpdate(is_active=False)
    updated_user = crud.user.update(db, db_obj=user, obj_in=user_update)
    return updated_user


@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = crud.user.remove(db, id=user_id)
    return deleted_user


@router.get("/reviews/", response_model=List[Review])
def read_reviews(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve reviews.
    """
    reviews = crud.review.get_multi(db, skip=skip, limit=limit)
    return reviews


@router.get("/")
def get_admin_dashboard_data(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    Retrieve admin dashboard data.
    """
    # This is a placeholder for the admin dashboard data
    return {"message": "Welcome to the admin dashboard!"}
