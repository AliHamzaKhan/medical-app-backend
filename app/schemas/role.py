
from typing import Optional

from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Role(RoleInDBBase):
    pass


# Properties properties stored in DB
class RoleInDB(RoleInDBBase):
    pass
