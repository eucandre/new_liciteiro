# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import Http404
from django.shortcuts import render
from .forms import *

def Cria_Tipo_licitacao(request):
  if request.method == 'POST':
    form = FormTiposLiciatacao(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormTiposLiciatacao()
  return render(request, 'app_licitacao/cria_tipo_licitacao.html', {'form': form})

def edita_Tipo_licitacao(request,nr_item):
  item = Tipos_de_Licitacao.objects.get(pk = nr_item)
  if request.method == 'POST':
    form = FormTiposLiciatacao(request.POST, instance = item)
    if form.is_valid():
      form.save()
  else:
    form = FormTiposLiciatacao(instance = item)
  return render(request, 'app_licitacao/cria_tipo_licitacao.html', {'form': form})


def Lista_tipo_licitacao(request):
  item_objeto = Tipos_de_Licitacao.objects.all()
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
  return render(request, "app_licitacao/tipos_licitacao/lista_tipos_licitacoes.html", {'item': item})


def item_tipo_licitacao(request, nr_item):
  try:
    item = Tipos_de_Licitacao.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_licitacao/tipos_licitacao/item_tipo_licitacao.html", {'item': item})



def Cria_Ato_licitacao(request):
  if request.method == 'POST':
    form = FormAtosLiciatacao(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormAtosLiciatacao()
  return render(request, 'app_licitacao/cria_ato_licitacao.html', {'form': form})

def edita_Ato_licitacao(request, nr_item):
  item = Atos_Licitacao.objects.get(pk = nr_item)
  if request.method == 'POST':
    form = FormAtosLiciatacao(request.POST, instance = item)
    if form.is_valid():
      form.save()
  else:
    form = FormAtosLiciatacao(instance = item)
  return render(request, 'app_licitacao/cria_ato_licitacao.html', {'form': form})

def Lista_ato_licitacao(request):
  item_objeto = Atos_Licitacao.objects.all()
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
  return render(request, "app_licitacao/atos_licitacao/lista_atos_licitacao.html", {'item': item})


def item_ato_licitacao(request, nr_item):
  try:
    item = Atos_Licitacao.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_licitacao/tipos_licitacao/item_tipo_licitacao.html", {'item': item})

def Cria_Modalidade_licitacao(request):
  if request.method == 'POST':
    form = FormModalidadeLiciatacao(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormModalidadeLiciatacao()
  return render(request, 'app_licitacao/cria_modalidade.html', {'form': form})

def edita_Modalidade_licitacao(request, nr_item):
  item = Modalidade_Licitacao.objects.get(pk = nr_item)
  if request.method == 'POST':
    form = FormModalidadeLiciatacao(request.POST, instance = item)
    if form.is_valid():
      form.save()
  else:
    form = FormModalidadeLiciatacao(instance = item)
  return render(request, 'app_licitacao/cria_modalidade.html', {'form': form})

def Lista_modalidade_licitacao(request):
  item_objeto = Modalidade_Licitacao.objects.all()
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
  return render(request, "app_licitacao/modalidades_licitacao/lista_modalidades_licitacao.html", {'item': item})


def item_modalidade_licitacao(request, nr_item):
  try:
    item = Modalidade_Licitacao.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_licitacao/modalidades_licitacao/item_modalidade_licitacao.html", {'item': item})
