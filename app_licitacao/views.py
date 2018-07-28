# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

def Cria_Ato_licitacao(request):
  if request.method == 'POST':
    form = FormAtosLiciatacao(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormAtosLiciatacao()
  return render(request, 'app_licitacao/cria_ato_licitacao.html', {'form': form})

def Cria_Modalidade_licitacao(request):
  if request.method == 'POST':
    form = FormModalidadeLiciatacao(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormModalidadeLiciatacao()
  return render(request, 'app_licitacao/cria_modalidade.html', {'form': form})

