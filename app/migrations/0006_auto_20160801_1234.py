# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 15:34
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_livro_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=stdimage.models.StdImageField(upload_to='capas'),
        ),
    ]