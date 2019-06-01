# import pytest
# from rest_framework import status
# from django.urls import reverse
# from django.test import Client, SimpleTestCase
# from brb.terminal_logs.models import Log
#
# pytestmark = pytest.mark.django_db
# log_in = pytest.mark.usefixtures('logged_in_user')
#
#
# @log_in
# def test_log_list(client: Client, helpers):
#     """It should return a valid response"""
#     response = client.get(reverse('terminal_logs:log_list'))
#     assert response.status_code == status.HTTP_200_OK
#
#     create_url = reverse('terminal_logs:create')
#     helpers.assertContains(response, create_url)
#
#
# @log_in
# def test_create_view_csrf(client, helpers):
#     response = client.get(reverse('terminal_logs:create'))
#     assert response.status_code == status.HTTP_200_OK
#
#     helpers.assertContains(response, 'form')
#     helpers.assertContains(response, 'csrfmiddlewaretoken')
#
#
# @log_in
# def test_create_view_valid_post(client: Client, helpers: SimpleTestCase):
#     """
#     A valid post should create a log and redirect the user to the log
#     detail page
#     """
#     url = reverse('terminal_logs:create')
#     data = {
#         'content': 'Adding some dummy content'
#     }
#     response = client.post(url, data, follow=True)
#     assert Log.objects.exists()
#     helpers.assertRedirects(response, reverse('terminal_logs:log_list'))
#
#
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
