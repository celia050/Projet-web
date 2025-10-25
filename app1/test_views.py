import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_api_test_endpoint():
    client = APIClient()
    response = client.get("/api/test/")
    assert response.status_code == 200
    assert response.json() == {"message": "Connexion OK"}  # <- utiliser .json() ici

