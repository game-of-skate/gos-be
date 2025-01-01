from django.db import models
from django.conf import settings


class TrickAbc(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        abstract = True


class TrickCommon(TrickAbc):
    class Meta:
        ordering = ("name",)
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_common_trick_name")
        ]

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"


class TrickPrivate(TrickAbc):
    parent = models.ForeignKey(
        TrickCommon,
        on_delete=models.SET_NULL,
        related_name="trick",
        null=True,
        blank=True,
        help_text="The common trick that this private trick is based on, if any",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tricks"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "user"], name="unique_personal_trick_name_per_user"
            )
        ]

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} for {self.user}"


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
    trick = models.ForeignKey(TrickPrivate, on_delete=models.CASCADE)
    set_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tricks_set"
    )
    # only necessary for distance games
    set_at = models.DateTimeField(auto_now_add=True)
