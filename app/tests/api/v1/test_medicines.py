from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.medicine import create_random_medicine
from app.tests.utils.user import create_random_user, user_authentication_headers
from app import crud
from app.schemas.medicine import MedicineCreate

def test_create_medicine(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {"name": "Foo", "manufacturer": "Bar", "dosage": "10mg"}
    response = client.post(
        f"{settings.API_V1_STR}/medicines/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content


def test_read_medicine(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    medicine = create_random_medicine(db)
    response = client.get(f"{settings.API_V1_STR}/medicines/{medicine.id}", headers=superuser_token_headers)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == medicine.name
    assert content["description"] == medicine.description
    assert content["id"] == medicine.id

def test_search_medicines(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    medicine = create_random_medicine(db)
    response = client.get(f"{settings.API_V1_STR}/medicines/?q={medicine.name}", headers=superuser_token_headers)
    assert response.status_code == 200
    content = response.json()
    assert len(content) > 0
    assert any(m["name"] == medicine.name for m in content)
