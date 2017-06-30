from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Team(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Game(models.Model):
    home_team_id = models.BigIntegerField()
    away_team_id = models.BigIntegerField()
    winning_team_id = models.BigIntegerField(null=True)
    difference_in_score = models.IntegerField(null=True)

    def __str__(self):
        home_team = Team.objects.get(pk=self.home_team_id)
        away_team = Team.objects.get(pk=self.away_team_id)
        retStr = home_team.name + ' vs ' + away_team.name