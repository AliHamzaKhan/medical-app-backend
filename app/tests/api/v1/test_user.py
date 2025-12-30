from app.main import app
from fastapi.testclient import TestClient
from app.core.config import settings


client = TestClient(app)

def get_bearer_token():
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    response = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    response.raise_for_status()  # Ensure the request was successful
    tokens = response.json()
    bearer_token = tokens["access_token"]
    return bearer_token