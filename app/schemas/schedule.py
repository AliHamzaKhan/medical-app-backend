from datetime import date, time
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ScheduleBase(BaseModel):
    doctor_id: Optional[int] = None
    date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None


class ScheduleCreate(ScheduleBase):
    doctor_id: int
    date: date
    start_time: time
    end_time: time


class ScheduleUpdate(ScheduleBase):
    pass


class ScheduleInDBBase(ScheduleBase):
    id: int
    doctor_id: int
    date: date
    start_time: time
    end_time: time

    model_config = ConfigDict(from_attributes=True)


class Schedule(ScheduleInDBBase):
    pass
