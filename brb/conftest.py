import pytest
from django.conf import settings
from django.test import RequestFactory

from brb.users.tests.factories import UserFactory


class DjangoHelpers:
    @staticmethod
    def assert_content(response, content):
        assert content in str(response.content)


@pytest.fixture()
def helpers():
    return DjangoHelpers


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


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
