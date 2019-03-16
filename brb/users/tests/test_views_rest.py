import pytest
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_seed_user(client, settings):
    """it should return a list of recipes in the database"""
    settings.DEBUG = True
    response = client.post('/integration/', format='json')
    assert response.status_code == status.HTTP_201_CREATED
    users = User.objects.all()
    assert users


@pytest.mark.django_db
@pytest.mark.xfail
def test_user_is_admin(client):
    """it should return a list of recipes in the database"""
    response = client.post('/integration/', format='json')
    assert response.status_code == status.HTTP_201_CREATED
    users = User.objects.all()
    assert False


@pytest.mark.django_db
def test_seed_user_non_dev_mode(client):
    """It should not seed the user if django is not in development mode"""
    response = client.post('/integration/', format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    users = User.objects.all()
    assert len(users) == 0
