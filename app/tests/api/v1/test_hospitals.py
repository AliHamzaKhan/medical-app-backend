
from typing import Dict
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.hospital import create_random_hospital
from app.tests.utils.utils import random_lower_string

def test_create_hospital(
    client: TestClient, db: Session
) -> None:
    data = {"name": "Foo", "address": "Bar", "latitude": 1.0, "longitude": 1.0}
    response = client.post(
        f"{settings.API_V1_STR}/hospitals/",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content

def test_read_hospital(
    client: TestClient, db: Session
) -> None:
    hospital = create_random_hospital(db)
    response = client.get(
        f"{settings.API_V1_STR}/hospitals/{hospital.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == hospital.name

def test_read_hospitals(
    client: TestClient, db: Session
) -> None:
    create_random_hospital(db)
    create_random_hospital(db)
    response = client.get(f"{settings.API_V1_STR}/hospitals/")
    assert response.status_code == 200
    content = response.json()
    assert len(content) >= 2

def test_update_hospital(
    client: TestClient, db: Session
) -> None:
    hospital = create_random_hospital(db)
    data = {"name": "Updated name"}
    response = client.put(
        f"{settings.API_V1_STR}/hospitals/{hospital.id}",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["id"] == hospital.id

def test_delete_hospital(
    client: TestClient, db: Session
) -> None:
    hospital = create_random_hospital(db)
    response = client.delete(
        f"{settings.API_V1_STR}/hospitals/{hospital.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == hospital.name

def test_upload_hospitals(
    client: TestClient, db: Session
) -> None:
    with open("app/tests/test_files/hospitals.xlsx", "rb") as f:
        response = client.post(
            f"{settings.API_V1_STR}/hospitals/upload-excel",
            files={"file": ("hospitals.xlsx", f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        )
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2


def test_upload_hospitals_invalid_file(
    client: TestClient, db: Session
) -> None:
    with open("app/tests/test_files/hospitals.xlsx", "rb") as f:
        response = client.post(
            f"{settings.API_V1_STR}/hospitals/upload-excel",
            files={"file": ("hospitals.txt", f, "text/plain")}
        )
    assert response.status_code == 400
