# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gram', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
