import pytest
from brb.terminal_logs.models import Log
from brb.users.tests.factories import UserFactory
from brb.terminal_logs.tests.factories import LogFactory


@pytest.mark.django_db
def test_logs_insert():
    user = UserFactory()
    log = LogFactory.build()
    Log.objects.create(log, user=user)
    assert Log.objects.count()
