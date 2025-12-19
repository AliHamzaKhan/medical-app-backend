from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.package import create_random_package


def test_create_package(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {"name": "Foo", "description": "Fighters", "price": 10.0, "credits": 10}
    response = client.post(
        f"{settings.API_V1_STR}/packages/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert content["price"] == data["price"]
    assert content["credits"] == data["credits"]
    assert "id" in content


def test_read_package(client: TestClient, db: Session) -> None:
    package = create_random_package(db)
    response = client.get(f"{settings.API_V1_STR}/packages/{package.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == package.name
    assert content["description"] == package.description
    assert content["price"] == package.price
    assert content["credits"] == package.credits
    assert content["id"] == package.id
