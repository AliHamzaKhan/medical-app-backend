from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.payment import Payment, PaymentCreate
from app.crud import payment

router = APIRouter()

@router.post("/", response_model=Payment)
def create_new_payment(payment_in: PaymentCreate, db: Session = Depends(deps.get_db)):
    return payment.create(db=db, obj_in=payment_in)

@router.get("/{payment_id}", response_model=Payment)
def read_payment(payment_id: int, db: Session = Depends(deps.get_db)):
    db_payment = payment.get(db, id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.get("/", response_model=list[Payment])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    payments = payment.get_multi(db, skip=skip, limit=limit)
    return payments
