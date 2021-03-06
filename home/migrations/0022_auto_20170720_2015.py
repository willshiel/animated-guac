# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-21 01:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_profile_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='away_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='home_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='home.Profile'),
        ),
    ]
