# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160815_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='anoNasc',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
