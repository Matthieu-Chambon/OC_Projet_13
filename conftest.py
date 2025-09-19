import pytest
from lettings.models import Address, Letting
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
def addresses():
    return [
        Address.objects.create(
            number=123,
            street="Rue principale",
            city="Paris",
            state="FR",
            zip_code=75000,
            country_iso_code="FRA",
        ),
        Address.objects.create(
            number=456,
            street="Avenue des Champs",
            city="Lyon",
            state="FR",
            zip_code=69000,
            country_iso_code="FRA",
        )
    ]


@pytest.fixture
def lettings(addresses):
    return [
        Letting.objects.create(
            title="Bel appartement au centre",
            address=addresses[0],
        ),
        Letting.objects.create(
            title="Maison avec jardin",
            address=addresses[1],
        )
    ]


@pytest.fixture
def profiles():
    return [
        Profile.objects.create(
            user=User.objects.create_user(
                username="Anonymous",
                first_name="John",
                last_name="Doe",
                email="john.doe@example.com",
                password="password"
            ),
            favorite_city="Nantes"
        ),
        Profile.objects.create(
            user=User.objects.create_user(
                username="Smiss",
                first_name="Smith",
                last_name="Anderson",
                email="smith.anderson@example.com",
                password="password"
            ),
            favorite_city="Rennes"
        )
    ]
