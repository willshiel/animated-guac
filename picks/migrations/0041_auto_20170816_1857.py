# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 23:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0040_auto_20170816_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='winning_team_id',
            new_name='winning_team',
        ),
    ]
