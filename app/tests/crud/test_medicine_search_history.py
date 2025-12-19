from sqlalchemy.orm import Session

from app import crud
from app.schemas.user import MedicineSearchHistoryCreate
from app.tests.utils.user import create_random_user


def test_create_medicine_search_history(db: Session) -> None:
    user = create_random_user(db)
    search_query = "Aspirin"
    history_in = MedicineSearchHistoryCreate(search_query=search_query)
    history = crud.medicine_search_history.create(db=db, obj_in=history_in, user_id=user.id)
    assert history.search_query == search_query
    assert history.user_id == user.id


def test_get_medicine_search_history(db: Session) -> None:
    user = create_random_user(db)
    search_query = "Ibuprofen"
    history_in = MedicineSearchHistoryCreate(search_query=search_query)
    history = crud.medicine_search_history.create(db=db, obj_in=history_in, user_id=user.id)
    stored_history = crud.medicine_search_history.get(db=db, id=history.id)
    assert stored_history
    assert stored_history.search_query == search_query
    assert stored_history.user_id == user.id


def test_get_multi_medicine_search_history_by_user(db: Session) -> None:
    user = create_random_user(db)
    search_query1 = "Paracetamol"
    history_in1 = MedicineSearchHistoryCreate(search_query=search_query1)
    crud.medicine_search_history.create(db=db, obj_in=history_in1, user_id=user.id)

    search_query2 = "Lisinopril"
    history_in2 = MedicineSearchHistoryCreate(search_query=search_query2)
    crud.medicine_search_history.create(db=db, obj_in=history_in2, user_id=user.id)

    history_list = crud.medicine_search_history.get_multi_by_user(db=db, user_id=user.id)
    assert len(history_list) == 2
