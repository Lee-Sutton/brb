from django.db import models


class ScoreCard(models.Model):
    score = models.IntegerField()
    slope = models.IntegerField(null=True)
    rating = models.FloatField(null=True)

    # TODO add owner
    # TODO allow users to share score cards ie. make them public or to a list of friends
    # TODO relate to course, attested, photo etc.

    def __str__(self):
        return f'Score: {self.score}'
