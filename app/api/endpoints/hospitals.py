from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import get_db
import pandas as pd

router = APIRouter()

@router.post("/", response_model=schemas.Hospital)
def create_hospital(hospital: schemas.HospitalCreate, db: Session = Depends(get_db)):
    hospital = crud.hospital.create(db=db, obj_in=hospital)
    db.commit()
    db.refresh(hospital)
    return hospital

@router.get("/{hospital_id}", response_model=schemas.Hospital)
def read_hospital(hospital_id: int, db: Session = Depends(get_db)):
    db_hospital = crud.hospital.get(db=db, id=hospital_id)
    if db_hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return db_hospital

@router.get("/", response_model=list[schemas.Hospital])
def read_hospitals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hospitals = crud.hospital.get_multi(db=db, skip=skip, limit=limit)
    return hospitals

@router.put("/{hospital_id}", response_model=schemas.Hospital)
def update_hospital(hospital_id: int, hospital: schemas.HospitalUpdate, db: Session = Depends(get_db)):
    db_hospital = crud.hospital.get(db=db, id=hospital_id)
    if db_hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    hospital = crud.hospital.update(db=db, db_obj=db_hospital, obj_in=hospital)
    db.commit()
    db.refresh(hospital)
    return hospital

@router.delete("/{hospital_id}", response_model=schemas.Hospital)
def delete_hospital(hospital_id: int, db: Session = Depends(get_db)):
    db_hospital = crud.hospital.get(db=db, id=hospital_id)
    if db_hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    hospital = crud.hospital.remove(db=db, id=hospital_id)
    db.commit()
    return hospital

@router.post("/upload-excel", response_model=list[schemas.Hospital])
def upload_hospitals(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Invalid file format")
    df = pd.read_excel(file.file)
    df.columns = [c.lower() for c in df.columns]
    hospitals = []
    for _, row in df.iterrows():
        hospital_in = schemas.HospitalCreate(**row.to_dict())
        hospital = crud.hospital.create(db=db, obj_in=hospital_in)
        hospitals.append(hospital)
    db.commit()
    for hospital in hospitals:
        db.refresh(hospital)
    return hospitals
