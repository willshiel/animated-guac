# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-18 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import picks.models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0028_auto_20170717_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='game_id',
        ),
        migrations.AddField(
            model_name='pick',
            name='away_team_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pick',
            name='away_team_name',
            field=models.CharField(default=picks.models.team_name_default, max_length=50),
        ),
        migrations.AddField(
            model_name='pick',
            name='home_team_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pick',
            name='home_team_name',
            field=models.CharField(default=picks.models.team_name_default, max_length=50),
        ),
    ]
