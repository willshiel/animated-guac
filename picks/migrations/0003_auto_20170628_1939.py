# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-29 00:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picks', '0002_auto_20170625_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='user',
        ),
        migrations.AddField(
            model_name='game',
            name='is_correct',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='game',
            name='picked_team',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Pick',
        ),
    ]
