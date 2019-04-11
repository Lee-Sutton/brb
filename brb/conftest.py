import pytest
from django.conf import settings
from django.test import RequestFactory, SimpleTestCase
from rest_framework.test import APIClient

from brb.users.tests.factories import UserFactory


@pytest.fixture()
def helpers():
    return SimpleTestCase()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture()
def logged_in_user(client, django_user_model):
    username = 'testuser'
    password = 'testpass'
    user = django_user_model.objects.create_user(username, password=password)
    logged_in = client.login(username=username, password=password)
    assert logged_in
    return user


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
