from fastapi.testclient import TestClient
from homework_3 import app
import pytest


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "We'd like to welcome"}
