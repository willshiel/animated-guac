from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    place = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name + ' ' + str(self.place)

class Record(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    ties = models.IntegerField(null=True)

    win_percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True)

    def __str__(self):
        return 'W: ' + str(self.wins) + ' L: ' + str(self.losses) + ' T: ' + str(self.ties)

def create_user_sub_models(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Record.objects.create(user=instance)

post_save.connect(create_user_sub_models, sender=User)
