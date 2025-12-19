
from typing import Dict
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.speciality import create_random_speciality

def test_create_speciality(
    client: TestClient, db: Session
) -> None:
    data = {"name": "Foo"}
    response = client.post(
        f"{settings.API_V1_STR}/specialities/",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content

def test_read_speciality(
    client: TestClient, db: Session
) -> None:
    speciality = create_random_speciality(db)
    response = client.get(
        f"{settings.API_V1_STR}/specialities/{speciality.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == speciality.name

def test_read_specialities(
    client: TestClient, db: Session
) -> None:
    create_random_speciality(db)
    create_random_speciality(db)
    response = client.get(f"{settings.API_V1_STR}/specialities/")
    assert response.status_code == 200
    content = response.json()
    assert len(content) >= 2

def test_update_speciality(
    client: TestClient, db: Session
) -> None:
    speciality = create_random_speciality(db)
    data = {"name": "Updated name"}
    response = client.put(
        f"{settings.API_V1_STR}/specialities/{speciality.id}",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["id"] == speciality.id

def test_delete_speciality(
    client: TestClient, db: Session
) -> None:
    speciality = create_random_speciality(db)
    response = client.delete(
        f"{settings.API_V1_STR}/specialities/{speciality.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == speciality.name
