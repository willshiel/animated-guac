from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)

class Game(models.Model):
    #id = models.AutoField(primary_key=True)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    winning_team = models.CharField(max_length=50)


class Pick(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picked_team = models.CharField(max_length=50)
    is_correct = models.BooleanField()

