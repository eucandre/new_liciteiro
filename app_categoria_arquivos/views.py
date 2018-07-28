# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *

def Cria_categoria_arquivos(request):
    if request.method == 'POST':
      form = FormCategoriaArquivos(request.POST)
      if form.is_valid():
        form.save()
    else:
      form = FormCategoriaArquivos()
    return render(request, 'app_objeto/cria_objeto.html', {'form': form})