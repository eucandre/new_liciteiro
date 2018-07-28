# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_cnaes.models import *

class Obejto(models.Model):
	nome = models.CharField(max_length = 500, unique = True)
	sessoes_cnaes = models.ManyToManyField(Cnaes_sessoes)
	ativo = models.BooleanField()
	
	def __unicode__(self):
		return self.nome
	
	class Meta:
		verbose_name_plural = 'Objeto para a operação, o que foi solicitado.'
