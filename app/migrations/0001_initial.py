# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Autor')),
                ('ano_nasc', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AutorLivro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Editora')),
            ],
        ),
        migrations.CreateModel(
            name='EditoraLivro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Editora')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('ano', models.DateField()),
                ('capa', models.ImageField(height_field=530, upload_to='capas', width_field=370)),
            ],
        ),
        migrations.AddField(
            model_name='editoralivro',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Livro'),
        ),
        migrations.AddField(
            model_name='autorlivro',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Livro'),
        ),
    ]