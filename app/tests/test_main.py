from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"http_requests_total" in response.content


def test_info():
    response = client.get("/api/info")
    assert response.status_code == 200
    body = response.json()
    assert "hostname" in body
    assert "python_version" in body
    assert "uptime_seconds" in body
