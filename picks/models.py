from django.db import models
from django.contrib.auth.models import User
from django import forms
from common.current_week import CURRENT_WEEK

def team_name_default():
    return {'name', 'place holder name'}

class Team(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    home_team_id = models.BigIntegerField()
    home_team_name = models.CharField(max_length=50, default=team_name_default)
    away_team_id = models.BigIntegerField()
    away_team_name = models.CharField(max_length=50, default=team_name_default)
    underdog = models.IntegerField(null=True)
    winning_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    margin = models.IntegerField(null=True)
    week = models.IntegerField(default=CURRENT_WEEK)

    def __str__(self):
        home_team = Team.objects.get(pk=self.home_team_id)
        away_team = Team.objects.get(pk=self.away_team_id)
        return home_team.name + ' vs ' + away_team.name

class Pick(models.Model):
    team_picked = models.ForeignKey(Team)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    is_correct = models.NullBooleanField()
    week = models.IntegerField(default=CURRENT_WEEK)
    margin = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=10)

    def __str__(self):
        return str(self.team_picked) + ' ' + str(self.user) + ' ' + str(self.week)
