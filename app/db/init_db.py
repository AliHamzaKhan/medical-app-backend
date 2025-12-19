
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db import initial_data
from app.db.base import Base
from app.db.session import engine

def init_db():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    initial_data.pre_populate_specialities(db)
    db.close()
