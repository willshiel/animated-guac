# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-22 19:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picks', '0032_remove_pick_home_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.NullBooleanField()),
                ('week', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='pick',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='pick',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pick',
            name='week',
        ),
        migrations.AlterField(
            model_name='pick',
            name='team_picked',
            field=models.CharField(default=b'Arsenal', max_length=50),
        ),
    ]
