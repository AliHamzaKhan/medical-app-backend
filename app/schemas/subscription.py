
from pydantic import BaseModel, ConfigDict
import datetime

class SubscriptionBase(BaseModel):
    user_id: int | None = None
    plan_id: int | None = None

class SubscriptionCreate(SubscriptionBase):
    user_id: int
    plan_id: int

class SubscriptionUpdate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    id: int
    start_date: datetime.datetime
    end_date: datetime.datetime
    user_id: int
    plan_id: int

    model_config = ConfigDict(from_attributes=True)
