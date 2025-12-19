from app.crud.base import CRUDBase
from app.models.user_subscription_plan import UserSubscriptionPlan
from app.schemas.user_subscription_plan import UserSubscriptionPlanCreate, UserSubscriptionPlanUpdate


class CRUDUserSubscriptionPlan(CRUDBase[UserSubscriptionPlan, UserSubscriptionPlanCreate, UserSubscriptionPlanUpdate]):
    pass


user_subscription_plan = CRUDUserSubscriptionPlan(UserSubscriptionPlan)
