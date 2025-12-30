from sqlalchemy.orm import Session
from datetime import date

from app import crud, schemas
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models.user import UserRole


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            first_name="Super",
            last_name="User",
            date_of_birth=date(1990, 1, 1),
            gender="Male",
            phone_number="1234567890",
            address="123 Superuser St",
            role=UserRole.SUPERUSER
        )
        user = crud.user.create(db, obj_in=user_in)
