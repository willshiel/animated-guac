from django.db import models
from django.contrib.auth.models import User

class League(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Record(models.Model):
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    win_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=50, null=False, default='Team Will')
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    has_picked = models.BooleanField(default=False)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, default=1)

class Schedule(models.Model):
    home_team = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='home_team', default=1)
    away_team = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='away_team', default=1)
    week = models.IntegerField(default=1)