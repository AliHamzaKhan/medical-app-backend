
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.medicine import create_random_medicine


def test_create_medicine(client: TestClient, superuser_token_headers: Dict[str, str], db: Session) -> None:
    data = {
        "name": "Test Medicine",
        "description": "This is a test medicine.",
        "url": "https://example.com/medicine.jpg"
    }
    response = client.post(
        f"{settings.API_V1_STR}/medicines/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200, response.json()
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert "id" in content


def test_read_medicine(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    medicine = create_random_medicine(db)
    response = client.get(f"{settings.API_V1_STR}/medicines/{medicine.id}", headers=superuser_token_headers)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == medicine.name
    assert content["description"] == medicine.description
    assert content["id"] == medicine.id
