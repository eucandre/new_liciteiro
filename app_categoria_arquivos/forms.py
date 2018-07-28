from django import forms
from .models import *

class FormCategoriaArquivos(forms.ModelForm):
  nome = forms.CharField(label = 'Nome da Categoria', max_length = 500,
                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
  ativo = forms.BooleanField(label = "Ativo",widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  class Meta:
    model = Categoria_Arquivos
    fields = ('nome','ativo')