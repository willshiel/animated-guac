# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-13 23:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0017_auto_20170712_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='opponent',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
        migrations.AddField(
            model_name='schedule',
            name='away_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedule',
            name='home_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to=settings.AUTH_USER_MODEL),
        ),
    ]
