from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base_class import Base

doctor_speciality_association = Table('doctor_speciality',
    Base.metadata,
    Column('doctor_id', Integer, ForeignKey('doctors.id')),
    Column('speciality_id', Integer, ForeignKey('specialities.id'))
)
