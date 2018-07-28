# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



UF = ((u'AC','AC'),(u'AL','AL'),(u'AP','AP'),(u'AM','AM'),(u'BA','BA'),(u'CE','CE'),(u'DF','DF'),(u'ES','ES'),
			(u'GO','GO'),(u'MA','MA'),(u'MT','MT'),(u'MS','MS'),(u'MG','MG'),(u'PA','PA'),(u'PB','PB'),
			(u'PR', 'PR'),(u'PE','PE'),(u'PI','PI'),(u'RJ','RJ'),(u'RN','RN'),(u'RS','RS'),(u'RO','RO'),(u'RR','RR'),
			(u'SC','SC'),(u'SP','SP'),(u'SE','SE'),(u'TO','TO'))

class Fonte(models.Model):
	nome = models.CharField(max_length=300)
	uf = models.CharField(max_length=2, choices = UF)
	data_criacao = models.DateTimeField(auto_now= True)
	ativo = models.BooleanField()

	def __unicode__(self):
		return self.nome

