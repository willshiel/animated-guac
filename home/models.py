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
    place = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    has_picked = models.BooleanField(default=False)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, default=1)