from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Role])
def read_roles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve roles.
    """
    roles = crud.role.get_multi(db, skip=skip, limit=limit)
    return roles


@router.post("/", response_model=schemas.Role)
def create_role(
    *, 
    db: Session = Depends(deps.get_db),
    role_in: schemas.RoleCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new role.
    """
    role = crud.role.create(db, obj_in=role_in)
    return role


@router.put("/{id}", response_model=schemas.Role)
def update_role(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    role_in: schemas.RoleUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a role.
    """
    role = crud.role.get(db, id=id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    role = crud.role.update(db, db_obj=role, obj_in=role_in)
    return role


@router.get("/{id}", response_model=schemas.Role)
def read_role(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get a specific role by id.
    """
    role = crud.role.get(db, id=id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.delete("/{id}", response_model=schemas.Role)
def delete_role(
    *, 
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete a role.
    """
    role = crud.role.get(db, id=id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    role = crud.role.remove(db, id=id)
    return role
