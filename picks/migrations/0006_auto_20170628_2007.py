# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-29 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0005_auto_20170628_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='user',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
