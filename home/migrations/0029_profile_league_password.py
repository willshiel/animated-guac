# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-01 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20170801_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='league_password',
            field=models.CharField(default=b'password', max_length=50),
        ),
    ]
