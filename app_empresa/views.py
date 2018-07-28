# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
import json
import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import *

def CriaEmpresa(request):
	
	if request.method == 'POST':
		form = FormEmpresa(request.POST)
		if form.is_valid():
			item = form.save(commit= False)
			response = requests.get('https://www.receitaws.com.br/v1/cnpj/'+item.cnpj)
			json = response.json()
			item.save()
			return render(request, 'app_empresas/cadastra_empresas.html', {'form':form, 'api':json})		
	else:

		form = FormEmpresa()
		
	return render(request, 'app_empresas/cadastra_empresas.html', {'form':form})

def Lista_empresas(request):
	item_empresa = Empresa.objects.all()
	paginator = Paginator(item_empresa, 2)
	page = request.GET.get('page')
	try:
		item = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		item = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		item = paginator.page(paginator.num_pages)
	return render(request, "app_empresas/lista_empresas.html", {'item':item})

def Detalha_empresa(request,nr_item):
	try:
		item = Empresa.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "app_empresas/item_empresa.html", {'item': item})