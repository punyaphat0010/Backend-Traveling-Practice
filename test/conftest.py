import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flasx.models.models import Base
from flasx.main import app
from fastapi.testclient import TestClient

TEST_DB_URL = "sqlite:///./pytest_temp.db"

@pytest.fixture(scope="function")
def client():
    # Setup: create a new test DB and tables
    engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    # Dependency override
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides = {}
    from flasx.routers import auth_router
    app.dependency_overrides[auth_router.get_db] = override_get_db
    client = TestClient(app)
    yield client

    # Teardown: drop all tables and remove file
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    if os.path.exists("pytest_temp.db"):
        os.remove("pytest_temp.db")
