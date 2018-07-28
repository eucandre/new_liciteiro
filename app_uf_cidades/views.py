# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from forms import *

def Cria_cidade(request):
  if request.method == 'POST':
    form = FormCidade(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormCidade()
  return render(request, 'app_uf_cidades/cria_uf_cidades.html', {'form': form})

def Cria_estado(request):
  if request.method == 'POST':
    form = FormCidade(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormCidade()
  return render(request, 'app_uf_cidades/cria_uf_cidades.html', {'form': form})
