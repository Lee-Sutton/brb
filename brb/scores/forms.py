from django.forms import ModelForm
from brb.scores.models import ScoreCard


class ScoreCardForm(ModelForm):
    class Meta:
        model = ScoreCard
        fields = ['score', 'slope', 'rating']
