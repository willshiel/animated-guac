from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    place = models.IntegerField()
    win_percentage = models.DecimalField(max_digits=5, decimal_places=2)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)