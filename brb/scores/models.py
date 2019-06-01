from django.db import models


class ScoreCard(models.Model):
    score = models.IntegerField()
    slope = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)

    # TODO relate to course, attested, photo etc.

    def __str__(self):
        return f'Score: {self.score}'
