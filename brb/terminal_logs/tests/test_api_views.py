import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from brb.terminal_logs.models import Log


@pytest.mark.django_db
def test_create_log(api_client: APIClient, django_user_model):
    """It should create a log"""
    username = 'testuser'
    password = 'testpass'

    user = django_user_model.objects.create_user(username, password=password)
    api_client.force_authenticate(user)

    data = {'content': 'Testing this out'}
    url = reverse('logs_api:crud')
    response = api_client.post(url, data=data)
    assert response.status_code == status.HTTP_201_CREATED
    log = Log.objects.get(**data)
    assert log is not None
    assert log.user is not None


@pytest.mark.django_db
def test_invalid_log(api_client: APIClient, django_user_model):
    """It should create a log"""
    username = 'testuser'
    password = 'testpass'

    user = django_user_model.objects.create_user(username, password=password)
    api_client.force_authenticate(user)

    url = reverse('logs_api:crud')
    response = api_client.post(url, data={})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Log.objects.count() == 0


@pytest.mark.django_db
def test_authentication_is_required(api_client: APIClient):
    """authentication is required to access the api"""
    url = reverse('logs_api:crud')
    response = api_client.post(url, data={})
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Log.objects.count() == 0


@pytest.mark.django_db
def test_only_owners_can_read(api_client: APIClient, django_user_model):
    """Only owners can view their logs"""
    # SETUP - create log for user 1
    username = 'testuser'
    password = 'testpass'

    user = django_user_model.objects.create_user(username, password=password)
    # TODO refactor to user factory
    Log.objects.create(content='Test content', user=user)

    # User 2 logs in
    username = 'testuser2'
    password = 'testpass'

    user2 = django_user_model.objects.create_user(username, password=password)
    api_client.force_authenticate(user2)

    url = reverse('logs_api:crud')
    response = api_client.get(url, data={})
    assert response.status_code == 200
    assert response.data is None
