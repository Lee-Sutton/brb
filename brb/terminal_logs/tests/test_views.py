import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
@pytest.mark.usefixtures('logged_in_user')
def test_log_list(client: Client, helpers):
    """It should return a valid response"""
    response = client.get(reverse('terminal_logs:log_list'))
    assert response.status_code == 200

    create_url = reverse('terminal_logs:create')
    helpers.assert_content(response, create_url)
