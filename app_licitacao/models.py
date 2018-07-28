# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tipos_de_Licitacao(models.Model):
	nome = models.CharField(max_length=300)
	sigla = models.CharField(max_length = 2)
	data_criacao = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return self.nome
	
	class Meta:
		verbose_name_plural = 'Tipos de Licitação'
		
class Modalidade_Licitacao(models.Model):
	nome = models.CharField(max_length = 150)
	ativo = models.BooleanField()
	data_criacao = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return self.nome

class Atos_Licitacao(models.Model):
	nome = models.CharField(max_length = 150)
	ativo = models.BooleanField()
	padrao = models.BooleanField()
	nova_data = models.BooleanField()
	data_criacao = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return self.nome