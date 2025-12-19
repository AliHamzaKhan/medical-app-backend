import enum
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class PaymentStatus(str, enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class Payment(Base):
    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))
    amount = Column(Float)
    payment_method = Column(String)
    transaction_id = Column(String)
    payment_status = Column(Enum(PaymentStatus))
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)

    appointment = relationship('Appointment')
