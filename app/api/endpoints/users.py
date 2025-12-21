from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import User, UserCreate
from app.crud.user import user

router = APIRouter()

@router.post("/", response_model=User)
def create_new_user(user_in: UserCreate, db: Session = Depends(deps.get_db)):
    return user.create(db=db, obj_in=user_in)

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(deps.get_db)):
    db_user = user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    users = user.get_multi(db, skip=skip, limit=limit)
    return users
