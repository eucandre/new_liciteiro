# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cnaes_divisoes(models.Model):
	id_divsao = models.CharField(max_length=10)
	descricao_divisao = models.CharField(max_length= 150)
	observacoes = models.TextField()
	nome_popupar = models.CharField(max_length=15000)

	def __unicode__(self):
		return self.descricao_divisao

	class Meta:
		verbose_name_plural = "Divisões das CNAES"

class Cnaes_sessoes(models.Model):
	id_sessao = models.CharField(max_length=5)
	descricao_sessao = models.CharField(max_length=300)
	divisao = models.ForeignKey(Cnaes_divisoes)

	def __unicode__(self):
		return self.descricao_sessao

	class Meta:
		verbose_name_plural = "Sessões das divisões das CNAES"

class Cnaes_grupos(models.Model):
	id_grupo = models.CharField(max_length=10)
	descricao_grupo = models.CharField(max_length=300)
	# aqui chama sessoes e divisoes
	sessao = models.ForeignKey(Cnaes_sessoes)
	observacoes = models.TextField()

	def __unicode__(self):
		return self.descricao_grupo

	class Meta:
		verbose_name_plural = "Grupos das sessões e das divisões das CNAES"

class Cnaes_classes(models.Model):
	id_classe = models.CharField(max_length=10)
	descricao_classe = models.CharField(max_length=300)
	# aqui chama sessoes e divisoes
	grupo = models.ForeignKey(Cnaes_grupos)
	observacoes = models.TextField()

	def __unicode__(self):
		return self.descricao_grupo

	class Meta:
		verbose_name_plural = "Classes dos grupos das sessões e das divisões das CNAES"

class Cnaes_sub_classes(models.Model):
	id_subclasse = models.CharField(max_length=10)
	descricao_sub_classe = models.CharField(max_length=300)
	# aqui chama sessoes e divisoes
	classe = models.ForeignKey(Cnaes_classes)
	observacoes = models.TextField()
	atividades = models.CharField(max_length=150000)
	def __unicode__(self):
		return self.descricao_grupo

	class Meta:
		verbose_name_plural = "Classes dos grupos das sessões e das divisões das CNAES"