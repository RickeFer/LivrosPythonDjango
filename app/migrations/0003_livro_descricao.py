# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_livro_capa'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='descricao',
            field=models.CharField(default='a', max_length=500),
            preserve_default=False,
        ),
    ]