# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-30 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20170720_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='team_name',
            field=models.CharField(max_length=50),
        ),
    ]
