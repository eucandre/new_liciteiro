# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Empresa(models.Model):
	
	cnpj= models.CharField(max_length=150)
	fantasia = models.CharField(max_length=300, blank = True, null = True)
	razao_social = models.CharField(max_length = 300, blank = True, null = True)
	atividade_principal = models.CharField(max_length=150, blank = True, null = True)
	atividades_secundarias = models.CharField(max_length=1500000, blank = True, null = True) 
	capital_social = models.CharField(max_length=150, blank = True, null = True) 
	data_situacao = models.CharField(max_length=150, blank = True, null = True)
	uf =  models.CharField(max_length=150, blank = True, null = True)
	natureza_juridica =  models.CharField(max_length=150, blank = True, null = True )
	abertura =  models.CharField(max_length=150, blank = True, null = True )
	situacao = models.CharField(max_length=150, blank = True, null = True )
	email = models.CharField(max_length=150, blank = True, null = True )
	telefone = models.CharField(max_length=150, blank = True, null = True )
	bairro = models.CharField(max_length=150, blank = True, null = True )
	cidade = models.CharField(max_length=150, blank = True, null = True )
	def __unicode__(self):
		return self.fantasia

	class Meta:
		verbose_name_plural = 'Empresa Cadastrada no Sistema'

