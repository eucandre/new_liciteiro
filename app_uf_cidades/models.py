# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Estado(models.Model):
	nome = models.CharField(max_length=150)
	acronimo = models.CharField(max_length=2)
	codigo = models.CharField(max_length=3)
	ativo = models.BooleanFeild()

	class Meta:
		verbose_name_plural = "Unidades Federativas da União"

	def __unicode__(self):
		return self.nome

class Cidade(model.Model):
	nome = models.CharField(max_length=300)
	estado = models.ForeignKey(Estado)
	codigo = models.CharField(max_length=5)
	ativo = models.BooleanFeild()
	data_criacao = models.DateTiemField(auto_now=True)

	def __unicode__(self):
		return self.nome

		class Meta:
		verbose_name_plural = "Cidades das Unidades Federativas da União"