# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-22 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0030_auto_20170718_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='pick',
            name='home_team',
            field=models.CharField(default=b'Arsenal', max_length=50),
        ),
    ]
