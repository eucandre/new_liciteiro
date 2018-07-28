# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

from .forms import *
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render

def Cria_fontes(request):
  if request.method == 'POST':
    form = FormFonte(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormFonte()
  return render(request, 'app_fontes/cria_fontes.html', {'form': form})


def Lista_fontes(request):
  item_objeto = Fonte.objects.all()
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
  return render(request, "app_fontes/lista_objetos.html", {'item': item})


def item_fonte(request, nr_item):
  try:
    item = Fonte.objects.get(pk = nr_item)
  except:
    raise Http404('Sem Registro!')
  return render(request, "app_fontes/item_fonte.html", {'item': item})

