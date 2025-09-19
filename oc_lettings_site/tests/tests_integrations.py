import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.conf.urls import handler500


@pytest.mark.django_db
def test_index(client):
    """Test d'intégration pour l'affichage de la page d'accueil"""
    # Test de la vue index
    url = reverse("index")
    response = client.get(url)

    # Vérifications spécifiques à la réponse
    assert response.status_code == 200
    assert "index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_404_page(client):
    """Test d'intégration pour une page non trouvée (404)"""
    # Test d'une URL inexistante
    url = "/non-existent-page/"
    response = client.get(url)

    # Vérifications spécifiques à la réponse
    assert response.status_code == 404
    assert "404.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_500_page(client):
    """Test d'intégration pour une erreur serveur (500)"""
    request = RequestFactory().get("/")
    # Simuler une erreur serveur en appelant directement le gestionnaire 500
    response = handler500(request)

    # Vérifications spécifiques à la réponse
    assert response.status_code == 500
    assert b"Une erreur interne est survenue" in response.content
