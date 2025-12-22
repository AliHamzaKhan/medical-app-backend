from sqlalchemy.orm import Session

from app import crud
from app.schemas.role import RoleCreate
from app.tests.utils.utils import random_lower_string

def create_random_role(db: Session):
    name = random_lower_string()
    role_in = RoleCreate(name=name)
    return crud.role.create(db=db, obj_in=role_in)
