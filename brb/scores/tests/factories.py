import random

from factory import DjangoModelFactory
from brb.scores.models import ScoreCard


class ScoreCardFactory(DjangoModelFactory):
    score = random.randint(0, 200)
    rating = random.randint(0, 200)
    slope = random.randint(0, 200)

    class Meta:
        model = ScoreCard

    # TODO add users to the score model
    # user = factory.SubFactory(UserFactory)
