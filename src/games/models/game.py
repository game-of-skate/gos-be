from django.db import models
from django.conf import settings


# TODO local is a bool? or 2 tables?
class Game(models.Model):
    name = models.CharField(max_length=150)
    started_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="games_started"
    )
    skaters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="games_played"
    )


class GameTrick(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="tricks")
    # TODO: your friends can see your private tricks? or copy them to your collection
    # for better data later, a record of all tricks you've tried?
    trick = models.ForeignKey("TrickPrivate", on_delete=models.CASCADE)
    set_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tricks_set"
    )
    # only necessary for distance games
    set_at = models.DateTimeField(auto_now_add=True)
