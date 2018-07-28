from django import forms
from .models import *


class FormFonte(forms.ModelForm):
  nome = forms.CharField(label = 'Nome da Categoria', max_length = 500,
                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
  uf = forms.ModelChoiceField(queryset = Cidade.objects.all(), widget = forms.Select(attrs = {'class':'form-control'}))
  ativo = forms.BooleanField(label = "Ativo", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  
  class Meta:
    model = Fonte
    fields = ('nome', 'uf', 'ativo')