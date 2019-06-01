import factory
from factory import DjangoModelFactory, Faker
from brb.scores.models import ScoreCard
from brb.users.tests.factories import UserFactory


class ScoreCardFactory(DjangoModelFactory):
    score = Faker('integer')
    slope = Faker('integer')
    rating = Faker('integer')

    class Meta:
        model = ScoreCard

    user = factory.SubFactory(UserFactory)
