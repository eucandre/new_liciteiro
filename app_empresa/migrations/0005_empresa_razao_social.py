# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-28 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_empresa', '0004_auto_20180718_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='razao_social',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]