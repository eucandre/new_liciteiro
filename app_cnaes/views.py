# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# -*- coding: utf-8 -*-

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import Http404
from django.shortcuts import render
from .forms import *


def Cria_cnaes_divisoes(request):
  if request.method == 'POST':
    form = FormCnaesDivisoes(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormCnaesDivisoes()
  return render(request, 'app_objeto/cria_objeto.html', {'form': form})


def lista_cnaes_divisoes(request):
  item_categorias_arquivos = Cnaes_divisoes.objects.all()
  paginator = Paginator(item_categorias_arquivos, 2)
  page = request.GET.get('page')
  try:
    item = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    item = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    item = paginator.page(paginator.num_pages)
  return render(request, "app_categoria_arquivos/lista_categorias_arquivos.html", {'item': item})


def item_cnaes_divisoes(request, nr_item):
  try:
    item = Cnaes_divisoes.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_categoria_arquivos/item_categoria_arquivos.html", {'item': item})

