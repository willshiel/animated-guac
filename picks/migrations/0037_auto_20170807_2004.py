# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-08 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0036_auto_20170804_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='difference_in_score',
            new_name='margin',
        ),
    ]
