# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria_Arquivos(models.Model):
	nome = models.CharField(max_length = 300)
	data_criacao = models.DateTimeField(auto_now= True)
	ativo = models.BooleanField()

	def __unicode__(self):
		return  self.nome


	class Meta:
		verbose_name_plural = "Categorias de Arquivos"
