from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
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
