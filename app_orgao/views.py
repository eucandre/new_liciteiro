# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.http import Http404
from django.shortcuts import render
from .forms import *
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

def Cria_orgao(request):
  if request.method == 'POST':
    form = FormOrgao(request.POST)
    if form.is_valid():
      item = form.save(commit = False)
      response = requests.get('https://www.receitaws.com.br/v1/cnpj/' + item.cnpj)
      json = response.json()
      item.save()
      return render(request, 'app_orgao/cria_orgao.html', {'form': form, 'api': json})
  else:
    
    form = FormOrgao()
  
  return render(request, 'app_orgao/cria_orgao.html', {'form': form})


def Lista_orgaos(request):
  item_objeto = Orgao.objects.all()
  paginator = Paginator(item_objeto, 2)
  page = request.GET.get('page')
  try:
    item = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    item = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    item = paginator.page(paginator.num_pages)
  return render(request, "app_orgao/lista_orgaos.html", {'item': item})


def item_orgao(request, nr_item):
  try:
    item = Orgao.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_orgao/item_orgao.html", {'item': item})

