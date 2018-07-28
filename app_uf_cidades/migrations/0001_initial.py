# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-28 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('codigo', models.CharField(max_length=5)),
                ('ativo', models.BooleanField()),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Cidades das Unidades Federativas da Uni\xe3o',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('acronimo', models.CharField(max_length=2)),
                ('codigo', models.CharField(max_length=3)),
                ('ativo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Unidades Federativas da Uni\xe3o',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_uf_cidades.Estado'),
        ),
    ]