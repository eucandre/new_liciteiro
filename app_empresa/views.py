# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
import requests

from .forms import *

# def cosuslta(item):
# 	response = requests.get('https://www.receitaws.com.br/v1/cnpj/'+item)
# 	json = response.json()
# 	return json

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
	item = Empresa.objects.all()
	return render(request, "app_empresas/lista_empresas.html", {'item':item})