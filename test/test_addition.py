from fastapi.testclient import TestClient
from app.main import app
from app.services.add_service import process_addition
import pytest

client = TestClient(app)


def test_process_request():
    response = client.post("/process", json={
        "batchid": "ide101",
        "payload": [[1, 2], [3, 4]]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "ide101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"


def test_empty_payload():
    response = client.post("/process", json={
        "batchid": "ide102",
        "payload": []
    })
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "ide102"
    assert data["response"] == []
    assert data["status"] == "complete"


def test_process_addition():
    assert process_addition([[1, 2], [3, 4]]) == [3, 7]
    assert process_addition([[5, 5], [10, 10]]) == [10, 20]
    assert process_addition([[], [1, 1]]) == [0, 2]
