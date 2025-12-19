from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.plan import create_random_plan


def test_create_plan(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {"name": "Foo", "description": "Fighters", "price": 10.0, "duration_days": 30}
    response = client.post(
        f"{settings.API_V1_STR}/plans/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert content["price"] == data["price"]
    assert content["duration_days"] == data["duration_days"]
    assert "id" in content


def test_read_plan(client: TestClient, db: Session) -> None:
    plan = create_random_plan(db)
    response = client.get(f"{settings.API_V1_STR}/plans/{plan.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == plan.name
    assert content["description"] == plan.description
    assert content["price"] == plan.price
    assert content["duration_days"] == plan.duration_days
    assert content["id"] == plan.id
