# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType, Field
from graphene_django.rest_framework.mutation import SerializerMutation

from brb.scores.models import ScoreCard
from brb.scores.serializers import ScoreCardSerializer


class ScoreCardType(DjangoObjectType):
    class Meta:
        model = ScoreCard


class Query(object):
    all_score_cards = graphene.List(ScoreCardType)

    def resolve_all_score_cards(self, info, **kwargs):
        return ScoreCard.objects.all()


# class ScoreCardMutation(DjangoModelFormMutation):
#     class Meta:
#         form_class = ScoreCardForm
#         # input_field_name = 'data'
#         # return_field_name = 'score_card'


class ScoreCardMutation(SerializerMutation):
    class Meta:
        serializer_class = ScoreCardSerializer
