# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-29 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0007_auto_20170628_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_id', models.BigIntegerField()),
                ('away_team_id', models.BigIntegerField()),
                ('winning_team_id', models.BigIntegerField()),
                ('difference_in_score', models.IntegerField()),
            ],
        ),
    ]
