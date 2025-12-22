from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Package)
def create_package(
    *, 
    db: Session = Depends(get_db), 
    package_in: schemas.PackageCreate
) -> Any:
    package = crud.package.create(db=db, obj_in=package_in)
    db.commit()
    db.refresh(package)
    return package

@router.get("/", response_model=List[schemas.Package])
def read_packages(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    packages = crud.package.get_multi(db, skip=skip, limit=limit)
    return packages

@router.get("/{id}", response_model=schemas.Package)
def read_package(
    *, 
    db: Session = Depends(get_db), 
    id: int
) -> Any:
    package = crud.package.get(db=db, id=id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package
