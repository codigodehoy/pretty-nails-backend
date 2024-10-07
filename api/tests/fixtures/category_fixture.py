import pytest

from api.main import app
from fastapi.testclient import TestClient
from ..mocks import mock_category


@pytest.fixture
def client():
    client = TestClient(app)
    return client

@pytest.fixture
def category():
    return mock_category()
