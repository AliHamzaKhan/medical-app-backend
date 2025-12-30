from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.utils import random_lower_string

def test_create_clinic(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {"name": "Foo Clinic", "address": "123 Foo Street"}
    response = client.post(
        f"{settings.API_V1_STR}/clinics/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["address"] == data["address"]
    assert "id" in content

def test_read_clinic(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    clinic_name = random_lower_string()
    clinic_address = random_lower_string()
    data = {"name": clinic_name, "address": clinic_address}
    response = client.post(
        f"{settings.API_V1_STR}/clinics/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    clinic_id = content["id"]

    response = client.get(
        f"{settings.API_V1_STR}/clinics/{clinic_id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == clinic_name
    assert content["address"] == clinic_address
    assert content["id"] == clinic_id
