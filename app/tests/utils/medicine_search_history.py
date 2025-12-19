from sqlalchemy.orm import Session
import random
import string
from app import crud, models
from app.schemas.user import MedicineSearchHistoryCreate
from app.tests.utils.user import create_random_user

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def create_random_medicine_search_history(db: Session) -> models.MedicineSearchHistory:
    user = create_random_user(db)
    search_query = random_lower_string()
    history_in = MedicineSearchHistoryCreate(search_query=search_query)
    return crud.medicine_search_history.create(db=db, obj_in=history_in, user_id=user.id)
