from typing import Dict

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.speciality import SpecialityCreate
from app.tests.utils.utils import random_lower_string


def test_create_speciality(
    client: TestClient, superuser_token_headers: Dict[str, str]
) -> None:
    """
    Test creating a new speciality.
    """
    data = {"name": random_lower_string()}
    response = client.post(
        f"{settings.API_V1_STR}/specialities/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content


def test_read_specialities(
    client: TestClient, superuser_token_headers: Dict[str, str], db: Session
) -> None:
    """
    Test reading specialities.
    """
    speciality_name = random_lower_string()
    speciality_in = SpecialityCreate(name=speciality_name)
    crud.speciality.create(db=db, obj_in=speciality_in)
    db.commit()

    response = client.get(
        f"{settings.API_V1_STR}/specialities/",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)
    assert any(s["name"] == speciality_name for s in content)
