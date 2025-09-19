import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_index(client):
    """Test d'intégration de la page listant tous les profils"""
    # Création des données de test
    profile_1 = Profile.objects.create(
        user=User.objects.create_user(
            username="Anonymous",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="password"
        ),
        favorite_city="Nantes"
    )
    profile_2 = Profile.objects.create(
        user=User.objects.create_user(
            username="Smiss",
            first_name="Smith",
            last_name="Anderson",
            email="smith.anderson@example.com",
            password="password"
        ),
        favorite_city="Rennes"
    )

    # Test de l'index des profils
    url = reverse("profiles_index")
    response = client.get(url)

    # Vérifications spécifiques à la réponse
    assert response.status_code == 200
    assert profile_1.user.username in response.content.decode()
    assert profile_2.user.username in response.content.decode()
    assert "profiles/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile(client):
    """Test d'intégration pour un profil spécifique"""
    # Création des données de test
    profile = Profile.objects.create(
        user=User.objects.create_user(
            username="Anonymous",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="password"
        ),
        favorite_city="Nantes"
    )

    # Test de la vue détaillant un profil spécifique
    url = reverse("profile", args=[profile.user.username])
    response = client.get(url)

    # Vérifications spécifiques à la réponse
    assert response.status_code == 200
    assert profile.user.username in response.content.decode()
    assert profile.user.first_name in response.content.decode()
    assert profile.user.last_name in response.content.decode()
    assert profile.user.email in response.content.decode()
    assert profile.favorite_city in response.content.decode()
    assert "profiles/profile.html" in [t.name for t in response.templates]
