from brb.scores.models import ScoreCard
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class ScoreCardList(ListView):
    model = ScoreCard


class ScoreCardDetail(DetailView):
    model = ScoreCard
