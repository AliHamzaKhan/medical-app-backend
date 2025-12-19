from fastapi import FastAPI
from app.api.api import api_router
from app.db.session import SessionLocal
from app.db.base import Base
from app.db.session import engine
from app.db.initial_data import pre_populate_specialities

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        pre_populate_specialities(db)
    finally:
        db.close()
