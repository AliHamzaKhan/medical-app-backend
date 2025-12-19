from pydantic import BaseModel
from datetime import datetime
from .appointment import Appointment
from app.models.payment import PaymentStatus

class PaymentBase(BaseModel):
    amount: float
    payment_method: str
    transaction_id: str
    payment_status: PaymentStatus

class PaymentCreate(PaymentBase):
    appointment_id: int

class Payment(PaymentBase):
    id: int
    payment_date: datetime
    appointment: Appointment

    class Config:
        from_attributes = True
