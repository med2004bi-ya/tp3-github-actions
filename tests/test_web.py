
import pytest
from app.web import create_app


# Fixture : préparer un client Flask réutilisable
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


# Test 1 : message normal
def test_moderate_message_normal(client):
    response = client.post(
        "/moderate",
        json={"message": "bonjour"}
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "decision": "autoriser"
    }


# Test 2 : message contenant SPAM en majuscules
def test_moderate_message_spam(client):
    response = client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "decision": "bloquer"
    }


# Test 3 : objet JSON vide
def test_moderate_message_absent(client):
    response = client.post(
        "/moderate",
        json={}
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Invalid message"
    }


# Test 4 : message avec un type incorrect
def test_moderate_message_nombre(client):
    response = client.post(
        "/moderate",
        json={"message": 42}
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Invalid message"
    }


# Bonus 1 : message composé uniquement d'espaces
def test_moderate_message_espaces(client):
    response = client.post(
        "/moderate",
        json={"message": "   "}
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Invalid message"
    }


# Bonus 2 : corps JSON de type liste
def test_moderate_json_liste(client):
    response = client.post(
        "/moderate",
        json=["bonjour", "spam"]
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "JSON object required"
    }
