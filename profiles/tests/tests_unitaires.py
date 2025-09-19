import pytest
from django.test import RequestFactory
from profiles.views import index as index_view
from profiles.views import profile as profile_view


@pytest.mark.django_db
def test_model_address(profiles):
    """Teste la représentation en chaîne d'un profil d'utilisateur"""
    profile = profiles[0]

    assert str(profile) == "Anonymous"


@pytest.mark.django_db
def test_view_index(mocker, profiles):
    """Teste la vue index des profils"""

    request = RequestFactory().get("/profiles/")
    response = index_view(request)

    assert response.status_code == 200
    assert "Anonymous" in response.content.decode()
    assert "Smiss" in response.content.decode()


@pytest.mark.django_db
def test_view_profile(mocker, profiles):
    """Teste la vue détaillant un profil spécifique"""
    profile = profiles[0]

    request = RequestFactory().get(f"/profiles/{profile.user.username}/")
    response = profile_view(request, profile.user.username)

    assert response.status_code == 200
    assert "Anonymous" in response.content.decode()
    assert "John" in response.content.decode()
    assert "Doe" in response.content.decode()
    assert "john.doe@example.com" in response.content.decode()
    assert "Nantes" in response.content.decode()


@pytest.mark.django_db
def test_url_index(client, profiles):
    """Teste l'URL de la page listant tous les profils"""
    response = client.get("/profiles/")

    assert response.status_code == 200
    assert "profiles/index.html" in [t.name for t in response.templates]
    assert "Anonymous" in response.content.decode()
    assert "Smiss" in response.content.decode()


@pytest.mark.django_db
def test_url_profile(client, profiles):
    """Teste l'URL de la page détaillant un profil spécifique"""
    profile = profiles[0]
    response = client.get(f"/profiles/{profile.user.username}/")

    assert response.status_code == 200
    assert "profiles/profile.html" in [t.name for t in response.templates]
    assert "Anonymous" in response.content.decode()
    assert "John" in response.content.decode()
    assert "Doe" in response.content.decode()
    assert "john.doe@example.com" in response.content.decode()
    assert "Nantes" in response.content.decode()
