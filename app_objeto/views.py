# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
