import pytest
from brb.scores import models
from brb.scores.tests.factories import ScoreCardFactory


@pytest.mark.django_db
def test_insert_scores():
    ScoreCardFactory.create()
    assert models.ScoreCard.objects.count()
