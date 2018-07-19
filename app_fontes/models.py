# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Fonte(models.Model):
	nome = models.CharField(max_length=300)
	uf = models.CharField(max_length=2)
	data_criacao = models.DateTimeField(auto_now= True)
	ativo = models.BooleanField()

	def __unicode__(self):
		return self.nome

