import factory
from factory import DjangoModelFactory, Faker
from brb.terminal_logs.models import Log
from brb.users.tests.factories import UserFactory


class LogFactory(DjangoModelFactory):
    content = Faker('text')

    class Meta:
        model = Log

    user = factory.SubFactory(UserFactory)
