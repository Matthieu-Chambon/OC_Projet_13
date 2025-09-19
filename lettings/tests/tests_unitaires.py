import pytest
from django.test import RequestFactory
from lettings.views import index as index_view
from lettings.views import letting as letting_view


@pytest.mark.django_db
def test_model_address(addresses):
    """Teste la représentation en chaîne d'une adresse"""
    address = addresses[0]

    assert str(address) == "123 Rue principale"


@pytest.mark.django_db
def test_model_letting(lettings):
    """Teste la représentation en chaîne d'une location"""
    letting = lettings[0]

    assert str(letting) == "Bel appartement au centre"


@pytest.mark.django_db
def test_view_index(mocker, lettings):
    """Teste la vue index des locations"""

    request = RequestFactory().get("/lettings/")
    response = index_view(request)

    assert response.status_code == 200
    assert "Bel appartement au centre" in response.content.decode()
    assert "Maison avec jardin" in response.content.decode()


@pytest.mark.django_db
def test_view_letting(mocker, lettings):
    """Teste la vue détaillant une location spécifique"""
    letting = lettings[0]

    request = RequestFactory().get(f"/lettings/{letting.id}/")
    response = letting_view(request, letting.id)

    assert response.status_code == 200
    assert "Bel appartement au centre" in response.content.decode()
    assert "123 Rue principale" in response.content.decode()


@pytest.mark.django_db
def test_url_index(client, lettings):
    """Teste l'URL de la page listant toutes les locations"""
    response = client.get("/lettings/")

    assert response.status_code == 200
    assert "lettings/index.html" in [t.name for t in response.templates]
    assert "Bel appartement au centre" in response.content.decode()
    assert "Maison avec jardin" in response.content.decode()


@pytest.mark.django_db
def test_url_letting(client, lettings):
    """Teste l'URL de la page détaillant une location spécifique"""
    letting = lettings[0]
    response = client.get(f"/lettings/{letting.id}/")

    assert response.status_code == 200
    assert "lettings/letting.html" in [t.name for t in response.templates]
    assert "Bel appartement au centre" in response.content.decode()
    assert "123 Rue principale" in response.content.decode()
