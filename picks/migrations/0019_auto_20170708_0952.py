# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-08 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0018_auto_20170706_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='away_team',
        ),
        migrations.RemoveField(
            model_name='pick',
            name='home_team',
        ),
    ]
