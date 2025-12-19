from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Any

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Package)
def create_package(
    *, 
    db: Session = Depends(deps.get_db),
    package_in: schemas.PackageCreate,
    current_user: models.User = Depends(deps.get_current_active_admin_user),
) -> Any:
    """
    Create new package.
    """
    package = crud.package.create(db=db, obj_in=package_in)
    return package

@router.get("/", response_model=List[schemas.Package])
def read_packages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve packages.
    """
    packages = crud.package.get_multi(db, skip=skip, limit=limit)
    return packages

@router.put("/{id}", response_model=schemas.Package)
def update_package(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    package_in: schemas.PackageUpdate,
    current_user: models.User = Depends(deps.get_current_active_admin_user),
) -> Any:
    """
    Update a package.
    """
    package = crud.package.get(db=db, id=id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    package = crud.package.update(db=db, db_obj=package, obj_in=package_in)
    return package

@router.delete("/{id}", response_model=schemas.Package)
def delete_package(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_admin_user),
) -> Any:
    """
    Delete a package.
    """
    package = crud.package.get(db=db, id=id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    package = crud.package.remove(db=db, id=id)
    return package

@router.post("/{package_id}/purchase", response_model=schemas.User)
def purchase_package(
    *, 
    db: Session = Depends(deps.get_db),
    package_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Purchase a package.
    """
    package = crud.package.get(db=db, id=package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")

    # Check if the package is for the user's role
    if package.role != current_user.role.name.lower():
        raise HTTPException(status_code=403, detail=f"This package is for {package.role}s only.")

    current_user.total_ai_credits += package.credits_granted
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
