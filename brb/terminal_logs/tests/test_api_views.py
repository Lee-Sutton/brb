import pytest
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
def test_create_log(api_client: APIClient, django_user_model):
    """It should create a log"""
    username = 'testuser'
    password = 'testpass'

    django_user_model.objects.create_user(username, password=password)
    logged_in = api_client.login(username=username, password=password)
    assert logged_in

    data = {'content': 'Testing this out'}

    response = api_client.post('/api/v1/logs/', data=data)
    assert response.status_code == status.HTTP_201_CREATED
