# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-13 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='percentage',
            new_name='win_percentage',
        ),
    ]