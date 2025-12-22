from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.role import create_random_role
from app.tests.utils.utils import random_lower_string

def test_create_role(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {"name": random_lower_string()}
    response = client.post(
        f"{settings.API_V1_STR}/roles/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]

def test_read_role(client: TestClient, db: Session) -> None:
    role = create_random_role(db)
    response = client.get(
        f"{settings.API_V1_STR}/roles/{role.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == role.name

def test_read_roles(client: TestClient, db: Session) -> None:
    create_random_role(db)
    create_random_role(db)
    response = client.get(f"{settings.API_V1_STR}/roles/")
    assert response.status_code == 200
    content = response.json()
    assert len(content) >= 2
