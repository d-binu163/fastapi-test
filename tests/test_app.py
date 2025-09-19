from fastapi.testclient import TestClient
from app import app  # replace `app` with your filename (without .py) if it's not app.py

client = TestClient(app)

def test_root_endpoint_not_found():
    """The root path `/` should return 404 since it is not defined."""
    response = client.get("/")
    assert response.status_code == 404

def test_valid_prediction():
    """Send valid patient data and expect a JSON response with prediction."""
    patient = {
        "age": 45,
        "sex": 1,
        "bmi": 25.3,
        "bp": 80.5,
        "s1": 0.1,
        "s2": -0.2,
        "s3": 0.05,
        "s4": -0.1,
        "s5": 0.3,
        "s6": -0.05
    }

    response = client.post("/predict", json=patient)
    assert response.status_code == 200
    json_data = response.json()
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], int)

def test_invalid_age():
    """Invalid age (-1) should fail validation."""
    patient = {
        "age": -1,   # invalid
        "sex": 1,
        "bmi": 25.3,
        "bp": 80.5,
        "s1": 0.1,
        "s2": -0.2,
        "s3": 0.05,
        "s4": -0.1,
        "s5": 0.3,
        "s6": -0.05
    }

    response = client.post("/predict", json=patient)
    assert response.status_code == 422  # Unprocessable Entity (validation error)

def test_invalid_sex():
    """Sex must be 0 or 1. If we send 2, validation should fail."""
    patient = {
        "age": 30,
        "sex": 2,  # invalid
        "bmi": 22.0,
        "bp": 75.0,
        "s1": 0.1,
        "s2": -0.2,
        "s3": 0.05,
        "s4": -0.1,
        "s5": 0.3,
        "s6": -0.05
    }

    response = client.post("/predict", json=patient)
    assert response.status_code == 422
