from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base_class import Base

doctor_speciality = Table(
    "doctor_speciality",
    Base.metadata,
    Column("doctor_id", Integer, ForeignKey("users.id")),
    Column("speciality_id", Integer, ForeignKey("speciality.id")),
)
