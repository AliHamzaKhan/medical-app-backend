from typing import Dict
from datetime import date, time

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.user import create_random_user


class TestSchedule:
    def test_create_schedule(self, client: TestClient, superuser_token_headers: Dict[str, str], db: Session) -> None:
        user, _ = create_random_user(db, client)
        data = {
            "doctor_id": user.id,
            "date": str(date(2024, 7, 26)),
            "start_time": str(time(9, 0, 0)),
            "end_time": str(time(17, 0, 0)),
            "is_available": True
            }
        response = client.post(
            f"{settings.API_V1_STR}/schedules/",
            headers=superuser_token_headers,
            json=data,
        )
        assert response.status_code == 200
        content = response.json()
        assert content["date"] == data["date"]
        assert content["start_time"] == data["start_time"]
        assert content["end_time"] == data["end_time"]
        assert "id" in content
        assert "doctor_id" in content

    def test_read_schedule(self, client: TestClient, superuser_token_headers: dict, db: Session) -> None:
        user, _ = create_random_user(db, client)
        schedule_data = {
            "doctor_id": user.id,
            "date": str(date(2024, 7, 26)),
            "start_time": str(time(9, 0, 0)),
            "end_time": str(time(17, 0, 0)),
            "is_available": True
        }
        response = client.post(
            f"{settings.API_V1_STR}/schedules/",
            headers=superuser_token_headers,
            json=schedule_data,
        )
        assert response.status_code == 200
        schedule_id = response.json()["id"]

        response = client.get(f"{settings.API_V1_STR}/schedules/{schedule_id}", headers=superuser_token_headers)
        assert response.status_code == 200
        content = response.json()
        assert content["date"] == schedule_data["date"]
        assert content["start_time"] == schedule_data["start_time"]
        assert content["end_time"] == schedule_data["end_time"]
        assert content["id"] == schedule_id
