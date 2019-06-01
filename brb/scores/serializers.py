from rest_framework import serializers
from brb.scores.models import ScoreCard


class ScoreCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreCard
        fields = ('id', 'score', 'slope', 'rating')
