# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-09 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0020_auto_20170708_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='team_picked',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
