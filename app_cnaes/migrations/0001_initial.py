# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cnaes_classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_classe', models.CharField(max_length=10)),
                ('descricao_classe', models.CharField(max_length=300)),
                ('observacoes', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Classes dos grupos das sess\xf5es e das divis\xf5es das CNAES',
            },
        ),
        migrations.CreateModel(
            name='Cnaes_divisoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_divsao', models.CharField(max_length=10)),
                ('descricao_divisao', models.CharField(max_length=150)),
                ('observacoes', models.TextField()),
                ('nome_popupar', models.CharField(max_length=15000)),
            ],
            options={
                'verbose_name_plural': 'Divis\xf5es das CNAES',
            },
        ),
        migrations.CreateModel(
            name='Cnaes_grupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_grupo', models.CharField(max_length=10)),
                ('descricao_grupo', models.CharField(max_length=300)),
                ('observacoes', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Grupos das sess\xf5es e das divis\xf5es das CNAES',
            },
        ),
        migrations.CreateModel(
            name='Cnaes_sessoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sessao', models.CharField(max_length=5)),
                ('descricao_sessao', models.CharField(max_length=300)),
                ('divisao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cnaes.Cnaes_divisoes')),
            ],
            options={
                'verbose_name_plural': 'Sess\xf5es das divis\xf5es das CNAES',
            },
        ),
        migrations.CreateModel(
            name='Cnaes_sub_classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_subclasse', models.CharField(max_length=10)),
                ('descricao_sub_classe', models.CharField(max_length=300)),
                ('observacoes', models.TextField()),
                ('atividades', models.CharField(max_length=150000)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cnaes.Cnaes_classes')),
            ],
            options={
                'verbose_name_plural': 'Classes dos grupos das sess\xf5es e das divis\xf5es das CNAES',
            },
        ),
        migrations.AddField(
            model_name='cnaes_grupos',
            name='sessao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cnaes.Cnaes_sessoes'),
        ),
        migrations.AddField(
            model_name='cnaes_classes',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cnaes.Cnaes_grupos'),
        ),
    ]
