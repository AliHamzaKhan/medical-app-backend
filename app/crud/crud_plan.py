from app.crud.base import CRUDBase
from app.models.plan import Plan
from app.schemas.plan import PlanCreate, PlanUpdate


class CRUDPlan(CRUDBase[Plan, PlanCreate, PlanUpdate]):
    pass


plan = CRUDPlan(Plan)
