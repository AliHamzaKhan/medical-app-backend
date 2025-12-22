from sqlalchemy.orm import Session

from app import crud
from app.schemas.package import PackageCreate

def create_random_package(db: Session) -> None:
    package_in = PackageCreate(
        name="Test Package",
        description="A package for testing",
        price=99.99,
        credits_granted=100,
        role="test"
    )
    return crud.package.create(db=db, obj_in=package_in)
