import pytest
from django.test import RequestFactory
from oc_lettings_site.views import index as index_view


@pytest.mark.django_db
def test_view_index():
    """Teste la vue page d'accueil"""

    request = RequestFactory().get("/")
    response = index_view(request)

    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()
