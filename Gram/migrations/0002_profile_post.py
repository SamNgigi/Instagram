# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Gram.Image'),
        ),
    ]