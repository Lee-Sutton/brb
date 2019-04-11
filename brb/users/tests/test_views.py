import pytest
from django.conf import settings
from django.test import RequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brb.users.views import UserRedirectView, UserUpdateView

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


class TestUserRedirectView:

    def test_get_redirect_url(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        view = UserRedirectView()
        request = request_factory.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestRestAuthViews(APITestCase):
    """Auth end points"""

    def setUp(self):
        self.user = {
            'username': 'lee',
            'email': 'lee@e.com',
            'password': 'secret'
        }

    def test_signup(self):
        new_user = {
            'username': 'lee',
            'email': 'lee@e.com',
            'password1': '@secret123',
            'password2': '@secret123'
        }
        response = self.client.post('/rest-auth/registration/',
                                    format='json', data=new_user)
        assert response.status_code == status.HTTP_201_CREATED
