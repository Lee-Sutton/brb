# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from brb.scores.models import ScoreCard


class ScoreCardType(DjangoObjectType):
    class Meta:
        model = ScoreCard


class Query(object):
    all_score_cards = graphene.List(ScoreCardType)

    def resolve_all_score_cards(self, info, **kwargs):
        return ScoreCard.objects.all()
