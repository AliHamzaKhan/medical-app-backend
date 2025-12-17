
from typing import Optional

from pydantic import BaseModel


# Shared properties
class RoleBase(BaseModel):
    name: Optional[str] = None


# Properties to receive on role creation
class RoleCreate(RoleBase):
    name: str


# Properties to receive on role update
class RoleUpdate(RoleBase):
    pass


# Properties shared by models in DB
class RoleInDBBase(RoleBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Role(RoleInDBBase):
    pass


# Properties properties stored in DB
class RoleInDB(RoleInDBBase):
    pass
