# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20170816_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='locked_matchups',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='league',
            name='locked_picks',
            field=models.BooleanField(default=False),
        ),
    ]
