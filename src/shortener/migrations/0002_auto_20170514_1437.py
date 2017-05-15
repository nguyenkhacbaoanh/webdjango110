# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KirrURLManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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