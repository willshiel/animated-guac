from django.db import models
from django.contrib.auth.models import User
from common.current_week import CURRENT_WEEK


class League(models.Model):
    name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=True, default='password')
    locked_picks = models.BooleanField(default=False)
    locked_matchups = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=50, null=False, unique=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    league_password = models.CharField(max_length=50, default='password')
    has_picked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.team_name)


class Record(models.Model):
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    win_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ': ' + self.win_percentage


class Schedule(models.Model):
    user_id = models.BigIntegerField(default=1)
    opponent = models.BigIntegerField(default=1)
    week = models.IntegerField(default=1)


class PointsForWeek(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.IntegerField(default=CURRENT_WEEK)
    points = models.IntegerField(default=0)