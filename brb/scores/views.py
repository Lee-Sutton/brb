from brb.scores.models import ScoreCard
from brb.scores.serializers import ScoreCardSerializer
from rest_framework import generics


class ScoreCardList(generics.ListCreateAPIView):
    queryset = ScoreCard.objects.all()
    serializer_class = ScoreCardSerializer


class ScoreCardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScoreCard.objects.all()
    serializer_class = ScoreCardSerializer
