from django.urls import path

from brb.scores.views import ScoreCardDetail, ScoreCardList

app_name = "scores"
urlpatterns = [
    path('', ScoreCardList.as_view(), name='list'),
    path('/<int:pk>/', ScoreCardDetail.as_view(), name='detail'),
]
