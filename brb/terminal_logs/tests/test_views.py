import pytest
from rest_framework import status
from django.urls import reverse
from django.test import Client

pytestmark = pytest.mark.django_db
log_in = pytest.mark.usefixtures('logged_in_user')


@log_in
def test_log_list(client: Client, helpers):
    """It should return a valid response"""
    response = client.get(reverse('terminal_logs:log_list'))
    assert response.status_code == status.HTTP_200_OK

    create_url = reverse('terminal_logs:create')
    helpers.assert_content(response, create_url)


@log_in
def test_create_view_csrf(client, helpers):
    response = client.get(reverse('terminal_logs:create'))
    assert response.status_code == status.HTTP_200_OK

    helpers.assert_content(response, 'form')
    helpers.assert_content(response, 'csrfmiddlewaretoken')
