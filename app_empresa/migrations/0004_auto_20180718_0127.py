# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_empresa', '0003_empresa_atividades_secundarias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='atividades_secundarias',
            field=models.CharField(blank=True, max_length=1500000, null=True),
        ),
    ]