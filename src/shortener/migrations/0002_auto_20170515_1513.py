# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-15 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='kirrurl',
            managers=[
                ('mode_random', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='kirrurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]