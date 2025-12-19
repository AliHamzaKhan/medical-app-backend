
from typing import Any, Dict, Optional, Union, List
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core import security
from app.crud.base import CRUDBase
from app.models.user import User
from app.models.speciality import Speciality
from app.models.clinic import Clinic
from app.schemas.user import UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=security.get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_active=obj_in.is_active,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if "password" in update_data and update_data["password"]:
            hashed_password = security.get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    def is_admin(self, user: User) -> bool:
        return user.role.name.lower() == "admin"

    def search_doctors(
        self, 
        db: Session, 
        *, 
        latitude: Optional[float] = None, 
        longitude: Optional[float] = None, 
        radius: Optional[float] = None, 
        speciality: Optional[str] = None, 
        hospital: Optional[str] = None, 
        name: Optional[str] = None, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[User]:
        query = db.query(User).filter(User.role.has(name='doctor'))

        if speciality:
            query = query.join(User.specialities).filter(Speciality.name.ilike(f"%{speciality}%"))

        if name:
            query = query.filter(User.full_name.ilike(f"%{name}%"))

        if hospital:
            query = query.join(User.clinics).filter(Clinic.name.ilike(f"%{hospital}%"))

        if latitude is not None and longitude is not None and radius is not None:
            # Haversine formula to calculate distance
            distance_subquery = (
                6371 * func.acos(
                    func.cos(func.radians(latitude)) * func.cos(func.radians(User.latitude)) * 
                    func.cos(func.radians(User.longitude) - func.radians(longitude)) + 
                    func.sin(func.radians(latitude)) * func.sin(func.radians(User.latitude))
                )
            ).label("distance")
            query = query.filter(distance_subquery <= radius)

        return query.offset(skip).limit(limit).all()


user = CRUDUser(User)
