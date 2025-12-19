from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.medicine import create_random_medicine
from app.tests.utils.user import create_random_user, user_authentication_headers
from app import crud

def test_create_medicine(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {"name": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/medicines/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert "id" in content


def test_read_medicine(client: TestClient, db: Session) -> None:
    medicine = create_random_medicine(db)
    response = client.get(f"{settings.API_V1_STR}/medicines/{medicine.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == medicine.name
    assert content["description"] == medicine.description
    assert content["id"] == medicine.id

def test_search_medicines_history(client: TestClient, db: Session) -> None:
    user, password = create_random_user(db)
    auth_headers = user_authentication_headers(client=client, email=user.email, password=password)
    medicine = create_random_medicine(db)

    response = client.get(f"{settings.API_V1_STR}/medicines/?q={medicine.name}", headers=auth_headers)
    assert response.status_code == 200

    history = crud.medicine_search_history.get_multi_by_user(db, user_id=user.id)
    assert len(history) == 1
    assert history[0].search_query == medicine.name
    assert history[0].user_id == user.id
    assert history[0].medicine_id == medicine.id
