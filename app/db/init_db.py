
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db import initial_data
from app.db.base_class import Base
from app.db.session import engine

def init_db():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    initial_data.create_initial_superuser(db)
    initial_data.create_initial_plans(db)
    db.close()
