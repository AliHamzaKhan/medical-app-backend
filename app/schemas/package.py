from pydantic import BaseModel, ConfigDict

class PackageBase(BaseModel):
    name: str
    description: str
    price: float
    credits_granted: int
    role: str

class PackageCreate(PackageBase):
    pass

class PackageUpdate(PackageBase):
    pass

class Package(PackageBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
