# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

from forms import *

def Cria_cidade(request):
  if request.method == 'POST':
    form = FormCidade(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormCidade()
  return render(request, 'app_uf_cidades/cria_uf_cidades.html', {'form': form})

def edita_cidade(request, nr_item):
  item = Cidade.objects.get(pk = nr_item)
  if request.method == 'POST':
    form = FormCidade(request.POST, instance = item)
    if form.is_valid():
      form.save()
  else:
    form = FormCidade(instance = item)
  return render(request, 'app_uf_cidades/cria_uf_cidades.html', {'form': form})

def Lista_estados(request):
  item_objeto = Estado.objects.all()
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
  return render(request, "app_uf_cidades/estados/lista_estados.html", {'item': item})


def item_estados(request, nr_item):
  try:
    item = Estado.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_uf_cidades/estados/item_estado.html", {'item': item})



def Lista_cidades(request):
  item_objeto = Cidade.objects.all()
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
  return render(request, "app_uf_cidades/cidades/lista_cidades.html", {'item': item})


def item_cidades(request, nr_item):
  try:
    item = Cidade.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_uf_cidades/cidades/item_cidade.html", {'item': item})


def Cria_estado(request):
  if request.method == 'POST':
    form = FormEstado(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormEstado()
  return render(request, 'app_uf_cidades/Cria_uf_estado.html', {'form': form})

def edita_estado(request, nr_item):
  item = Estado.objects.get(pk = nr_item)
  if request.method == 'POST':
    form = FormCidade(request.POST, instance = item)
    if form.is_valid():
      form.save()
  else:
    form = FormCidade(instance = item)
  return render(request, 'app_uf_cidades/Cria_uf_estado.html', {'form': form})
