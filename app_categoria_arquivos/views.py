# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import Http404
from django.shortcuts import render
from .forms import *

def Cria_categoria_arquivos(request):
    if request.method == 'POST':
      form = FormCategoriaArquivos(request.POST)
      if form.is_valid():
        form.save()
    else:
      form = FormCategoriaArquivos()
    return render(request, 'app_categoria_arquivos/cria_categoria_arquivos.html', {'form': form})


def edita_categoria_arquivos(request, nr_item):
  item = Categoria_Arquivos.objects.get(pk = nr_item)
  if request.method == 'POST':
    form = FormCategoriaArquivos(request.POST, instance = item)
    if form.is_valid():
      form.save()
  else:
    form = FormCategoriaArquivos(instance = item)
  return render(request, 'app_categoria_arquivos/cria_categoria_arquivos.html', {'form': form})


def lista_categorias_arquivos(request):
  item_categorias_arquivos = Categoria_Arquivos.objects.all()
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

def item_categorias_arquivos(request, nr_item):
  try:
    item = Categoria_Arquivos.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_categoria_arquivos/item_categoria_arquivos.html", {'item': item})
  