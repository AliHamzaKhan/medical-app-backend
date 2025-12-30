from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app import crud
from app.schemas.medicine_search_history import MedicineSearchHistoryCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_medicine_search_history(db: Session, client: TestClient) -> None:
    user, _ = create_random_user(db, client)
    search_query = random_lower_string()
    search_history_in = MedicineSearchHistoryCreate(search_query=search_query, user_id=user.id)
    search_history = crud.medicine_search_history.create(db=db, obj_in=search_history_in)
    assert search_history
    assert search_history.search_query == search_query
    assert search_history.user_id == user.id


def test_get_medicine_search_history(db: Session, client: TestClient) -> None:
    user, _ = create_random_user(db, client)
    search_query = random_lower_string()
    search_history_in = MedicineSearchHistoryCreate(search_query=search_query, user_id=user.id)
    search_history = crud.medicine_search_history.create(db=db, obj_in=search_history_in)
    stored_search_history = crud.medicine_search_history.get(db=db, id=search_history.id)
    assert stored_search_history
    assert stored_search_history.search_query == search_query
    assert stored_search_history.user_id == user.id


def test_get_multi_medicine_search_history_by_user(db: Session, client: TestClient) -> None:
    user, _ = create_random_user(db, client)
    search_query1 = random_lower_string()
    search_history_in1 = MedicineSearchHistoryCreate(search_query=search_query1, user_id=user.id)
    crud.medicine_search_history.create(db=db, obj_in=search_history_in1)

    search_query2 = random_lower_string()
    search_history_in2 = MedicineSearchHistoryCreate(search_query=search_query2, user_id=user.id)
    crud.medicine_search_history.create(db=db, obj_in=search_history_in2)

    search_history = crud.medicine_search_history.get_multi_by_user(db=db, user_id=user.id)
    assert search_history
    assert len(search_history) == 2
