# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 01:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0034_auto_20170816_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='profile',
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(default=39, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]