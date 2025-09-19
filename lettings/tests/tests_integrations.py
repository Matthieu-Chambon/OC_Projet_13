import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index(client):
    """Test d'intégration de la page listant toutes les locations"""
    # Création des données de test
    address_1 = Address.objects.create(
        number=123,
        street="Rue principale",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA"
    )
    address_2 = Address.objects.create(
        number=456,
        street="Avenue des Champs",
        city="Lyon",
        state="FR",
        zip_code=69000,
        country_iso_code="FRA"
    )

    Letting.objects.create(
        title="Bel appartement au centre",
        address=address_1
    )
    Letting.objects.create(
        title="Maison avec jardin",
        address=address_2
    )

    # Test de l'index des locations
    url = reverse("lettings_index")
    response = client.get(url)

    # Vérifications spécifiques à la réponse
    assert response.status_code == 200
    assert "Bel appartement au centre" in response.content.decode()
    assert "Maison avec jardin" in response.content.decode()
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_letting(client):
    """Test d'intégration pour une location spécifique"""
    # Création des données de test
    address = Address.objects.create(
        number=123,
        street="Rue principale",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(
        title="Bel appartement au centre",
        address=address
    )

    # Test de la vue détaillant une location spécifique
    url = reverse("letting", args=[letting.id])
    response = client.get(url)

    # Vérifications spécifiques à la réponse
    assert response.status_code == 200
    assert "Bel appartement au centre" in response.content.decode()
    assert "123 Rue principale" in response.content.decode()
    assert "lettings/letting.html" in [t.name for t in response.templates]
