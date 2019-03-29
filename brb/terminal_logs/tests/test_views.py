import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_log_list(user, client: Client):
    """It should return a valid response"""
    client.login(username=user.username, password=user.password)
    response = client.get(reverse('terminal_logs:log_list'), follow=True)
    assert response.status_code == 200
