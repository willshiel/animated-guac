# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-02 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import picks.models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0009_auto_20170628_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='away_team_name',
            field=models.CharField(default=picks.models.team_name_default, max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team_name',
            field=models.CharField(default=picks.models.team_name_default, max_length=50),
        ),
    ]
