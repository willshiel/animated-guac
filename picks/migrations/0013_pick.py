# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-03 01:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picks', '0012_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picks.Game')),
                ('team_picked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picks.Team')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
