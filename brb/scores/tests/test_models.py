import pytest
from brb.scores import models
from brb.scores.tests.factories import ScoreCardFactory


@pytest.mark.django_db
def test_logs_insert():
    ScoreCardFactory.create()
    assert models.ScoreCard.objects.count()
