# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import Http404
from django.shortcuts import render
from .forms import *

def Cria_Objeto(request):
  item = Objeto.objects.all()# fica aqui por precaucao
  if request.method == 'POST':
    form = FormObjeto(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormObjeto()
  return render(request, 'app_objeto/cria_objeto.html', {'form':form})

def Lista_objetos(request):
  item_objeto = Objeto.objects.all()
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
  return render(request, "app_objeto/lista_objetos.html", {'item': item})

def item_objeto(request, nr_item):
  try:
    item = Objeto.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_objeto/item_objeto.html", {'item': item})
 