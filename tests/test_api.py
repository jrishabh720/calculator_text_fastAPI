from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_calculator_addition():
    response = client.post(
        "/tools/calculator",
        json={
            "a": 10,
            "b": 5,
            "operation": "add",
        },
    )

    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_calculator_division_by_zero():
    response = client.post(
        "/tools/calculator",
        json={
            "a": 10,
            "b": 0,
            "operation": "divide",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Cannot divide by zero"
    )


def test_calculator_invalid_operation():
    response = client.post(
        "/tools/calculator",
        json={
            "a": 10,
            "b": 5,
            "operation": "unknown",
        },
    )

    assert response.status_code == 422


def test_text_uppercase():
    response = client.post(
        "/tools/text",
        json={
            "text": "hello world",
            "operation": "uppercase",
        },
    )

    assert response.status_code == 200
    assert response.json()["result"] == "HELLO WORLD"


def test_text_word_count():
    response = client.post(
        "/tools/text",
        json={
            "text": "FastAPI Agent Engineering",
            "operation": "word_count",
        },
    )

    assert response.status_code == 200
    assert response.json()["result"] == 3


def test_get_calculator_information():
    response = client.get("/tools/calculator")

    assert response.status_code == 200

    data = response.json()

    assert data["tool_id"] == "calculator"
    assert data["name"] == "Calculator"
    assert "add" in data["operations"]


def test_unknown_tool():
    response = client.get("/tools/unknown")

    assert response.status_code == 404
    assert response.json()["detail"] == (
        "Tool not found: unknown"
    )