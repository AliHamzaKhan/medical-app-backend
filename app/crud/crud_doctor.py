
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash
from app.crud import crud_role


class CRUDDoctor(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            role=crud_role.role.get_by_name(db, name="doctor"),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


doctor = CRUDDoctor(User)
