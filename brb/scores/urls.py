from django.urls import path

from brb.scores.views import ScoreCardList, ScoreCardDetail

app_name = "scores"
urlpatterns = [
    path('', view=ScoreCardList.as_view(), name="list"),
    path('/<int:pk>/', ScoreCardDetail.as_view()),
]
