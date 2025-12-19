from sqlalchemy.orm import Session
import datetime
from app.crud.base import CRUDBase

from app.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate
from app import crud

class CRUDSubscription(CRUDBase[Subscription, SubscriptionCreate, SubscriptionUpdate]):
    def create(self, db: Session, *, obj_in: SubscriptionCreate) -> Subscription:
        plan = crud.plan.get(db, id=obj_in.plan_id)
        end_date = datetime.datetime.utcnow() + datetime.timedelta(days=plan.duration_days)
        db_obj = Subscription(
            user_id=obj_in.user_id,
            plan_id=obj_in.plan_id,
            end_date=end_date,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_subscriptions_by_user(self, db: Session, user_id: int, skip: int = 0, limit: int = 100) -> list[Subscription]:
        return db.query(self.model).filter(self.model.user_id == user_id).offset(skip).limit(limit).all()


subscription = CRUDSubscription(Subscription)
