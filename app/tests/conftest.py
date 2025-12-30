import pytest
from typing import Generator, Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.db.init_db import init_db
from app.tests.utils.utils import get_superuser_token_headers

@pytest.fixture(scope="function")
def db() -> Generator:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    init_db(db)
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db: Session) -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def superuser_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return get_superuser_token_headers(client, db)
