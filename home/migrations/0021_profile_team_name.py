# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-21 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_schedule_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='team_name',
            field=models.CharField(default=b'Team Will', max_length=50),
        ),
    ]