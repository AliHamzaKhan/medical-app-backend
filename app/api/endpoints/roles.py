from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.role.create(db=db, obj_in=role)

@router.get("/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.role.get(db=db, id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.get("/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.role.get_multi(db=db, skip=skip, limit=limit)
    return roles

@router.put("/{role_id}", response_model=schemas.Role)
def update_role(role_id: int, role: schemas.RoleUpdate, db: Session = Depends(get_db)):
    db_role = crud.role.get(db=db, id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return crud.role.update(db=db, db_obj=db_role, obj_in=role)

@router.delete("/{role_id}", response_model=schemas.Role)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.role.get(db=db, id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return crud.role.remove(db=db, id=role_id)
