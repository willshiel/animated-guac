# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-29 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0008_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='difference_in_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='winning_team_id',
            field=models.BigIntegerField(null=True),
        ),
    ]