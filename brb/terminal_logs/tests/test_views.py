import pytest
from django.urls import reverse
from django.test import Client

from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_log_list(client: Client):
    """It should return a valid response"""
    username = 'testuser'
    password = 'testpass'
    User = get_user_model()
    User.objects.create_user(username, password=password)
    logged_in = client.login(username=username, password=password)

    assert logged_in
    response = client.get(reverse('terminal_logs:log_list'))
    assert response.status_code == 200

    create_url = reverse('terminal_logs:create')
    assert create_url in str(response.content)
