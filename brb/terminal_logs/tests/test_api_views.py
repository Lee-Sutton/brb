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
    assert Log.objects.filter(**data)
