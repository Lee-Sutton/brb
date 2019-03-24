from factory import DjangoModelFactory, Faker
from brb.terminal_logs.models import Log


class LogFactory(DjangoModelFactory):
    content = Faker('text')

    class Meta:
        model = Log
