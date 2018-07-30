# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_cnaes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500, unique=True)),
                ('ativo', models.BooleanField()),
                ('sessoes_cnaes', models.ManyToManyField(to='app_cnaes.Cnaes_sessoes')),
            ],
            options={
                'verbose_name_plural': 'Objeto para a opera\xe7\xe3o, o que foi solicitado.',
            },
        ),
    ]
