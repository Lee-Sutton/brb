import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

pytestmark = pytest.mark.django_db
log_in = pytest.mark.usefixtures('logged_in_user')


@pytest.mark.django_db
def test_create_score(api_client: APIClient, django_user_model):
    """The api should create a score"""
    # username = 'testuser'
    # password = 'testpass'
    #
    # django_user_model.objects.create_user(username, password=password)
    # logged_in = api_client.login(username=username, password=password)
    # assert logged_in

    data = {
        'score': 72,
        'slope': 135,
        'rating': 72.1
    }

    response = api_client.post('/api/v1/scores', data=data)
    assert response.status_code == status.HTTP_201_CREATED


# @log_in
# def test_create_view_invalid_post(client: Client):
#     """
#     A valid post should create a log and redirect the user to the log
#     detail page
#     """
#     url = reverse('terminal_logs:create')
#     response = client.post(url, data={}, follow=True)
#     assert not Log.objects.exists()
#     assert response.status_code == status.HTTP_200_OK
