# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render
from .forms import *

def Cria_orgao(request):
  if request.method == 'POST':
    form = FormOrgao(request.POST)
    if form.is_valid():
      item = form.save(commit = False)
      response = requests.get('https://www.receitaws.com.br/v1/cnpj/' + item.cnpj)
      json = response.json()
      item.save()
      return render(request, 'app_empresas/cadastra_empresas.html', {'form': form, 'api': json})
  else:
    
    form = FormOrgao()
  
  return render(request, 'app_empresas/cadastra_empresas.html', {'form': form})

