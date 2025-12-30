
from typing import Any, List, Optional

from fastapi import APIRouter, Body, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from .... import crud, models, schemas
from ... import deps
from ....core.config import settings
from ....crud import crud_doctor

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(
    *, 
    db: Session = Depends(deps.get_db), 
    user_in: schemas.UserCreate
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.get("/doctors/nearby/", response_model=List[schemas.User])
def get_nearby_doctors(
    latitude: float = Query(..., description="Latitude of the user"),
    longitude: float = Query(..., description="Longitude of the user"),
    max_distance: float = Query(10.0, description="Maximum distance in kilometers"),
    specialization: Optional[str] = Query(None, description="Doctor's specialization"),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get nearby doctors.
    """
    doctors = crud_doctor.doctor.get_nearby_doctors(
        db, latitude=latitude, longitude=longitude, max_distance=max_distance, specialization=specialization
    )
    return doctors
