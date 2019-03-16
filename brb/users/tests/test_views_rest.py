import pytest
from rest_framework import status
from django.contrib.auth import get_user_model
from brb.users.views_integration import TEST_USER

User = get_user_model()


@pytest.mark.django_db
def test_seed_user(client, settings):
    """it should return a list of recipes in the database"""
    settings.DEBUG = True
    response = client.post('/integration/', format='json')
    assert response.status_code == status.HTTP_201_CREATED
    user = User.objects.get(username=TEST_USER['username'])
    assert user
    assert user.is_superuser


@pytest.mark.django_db
def test_seed_user_non_dev_mode(client):
    """It should not seed the user if django is not in development mode"""
    response = client.post('/integration/', format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    users = User.objects.all()
    assert len(users) == 0
