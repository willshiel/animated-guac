# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-13 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0021_auto_20170709_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='matchweek',
            field=models.IntegerField(default=1),
        ),
    ]
