from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime

# default for team name fields and matchweek
def team_name_default():
    return {'name', 'place holder name'}

def matchweek_default():
    return {'week', datetime.now }

class Team(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Game(models.Model):
    home_team_id = models.BigIntegerField()
    home_team_name = models.CharField(max_length=50, default=team_name_default)
    away_team_id = models.BigIntegerField()
    away_team_name = models.CharField(max_length=50, default=team_name_default)
    winning_team_id = models.BigIntegerField(null=True)
    difference_in_score = models.IntegerField(null=True)
    matchweek = models.DateTimeField()

    def __str__(self):
        home_team = Team.objects.get(pk=self.home_team_id)
        away_team = Team.objects.get(pk=self.away_team_id)
        retStr = home_team.name + ' vs ' + away_team.name

class Pick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_picked = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    is_correct = models.NullBooleanField()
    matchweek = models.DateTimeField()