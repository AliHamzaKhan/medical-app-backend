from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

from app.models.payment import PaymentStatus

# Shared properties
class PaymentBase(BaseModel):
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None
    payment_status: Optional[PaymentStatus] = None
    payment_date: Optional[datetime] = None


# Properties to receive on item creation
class PaymentCreate(PaymentBase):
    appointment_id: int
    amount: float
    payment_method: str


# Properties to receive on item update
class PaymentUpdate(PaymentBase):
    pass


# Properties shared by models in DB
class PaymentInDBBase(PaymentBase):
    id: int
    appointment_id: int

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Payment(PaymentInDBBase):
    pass


# Properties properties stored in DB
class PaymentInDB(PaymentInDBBase):
    pass
