from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Payment])
def read_payments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve payments.
    """
    if crud.user.is_superuser(current_user):
        payments = crud.payment.get_multi(db, skip=skip, limit=limit)
    else:
        payments = crud.payment.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return payments


@router.post("/", response_model=schemas.Payment)
def create_payment(
    *,
    db: Session = Depends(deps.get_db),
    payment_in: schemas.PaymentCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new payment.
    """
    payment = crud.payment.create_with_owner(db=db, obj_in=payment_in, owner_id=current_user.id)
    return payment


@router.get("/{id}", response_model=schemas.Payment)
def read_payment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get payment by ID.
    """
    payment = crud.payment.get(db=db, id=id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    if not crud.user.is_superuser(current_user) and (payment.appointment.patient_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return payment
