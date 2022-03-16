from main import app
import pytest
import flask


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
