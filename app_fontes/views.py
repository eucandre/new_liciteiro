# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import *

from django.shortcuts import render

def Cria_fontes(request):
  if request.method == 'POST':
    form = FormFonte(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormFonte()
  return render(request, 'app_fontes/cria_fontes.html', {'form': form})
