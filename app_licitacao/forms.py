# coding=utf-8
from django import forms

from .models import *

class FormTiposLiciatacao(forms.ModelForm):
  nome = forms.CharField(label = 'Tipo', max_length = 500,
                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
  sigla = forms.CharField(label = 'Sigla', max_length = 10,
                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
  class Meta:
    model = Tipos_de_Licitacao
    fields = ('nome', 'sigla')

class FormModalidadeLiciatacao(forms.ModelForm):
  nome = forms.CharField(label = 'Modalidade', max_length = 500,
                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
  ativo = forms.BooleanField(label = "Ativo", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  
  class Meta:
    model = Modalidade_Licitacao
    fields = ('nome', 'ativo')

class FormAtosLiciatacao(forms.ModelForm):
  nome = forms.CharField(label = 'Ato', max_length = 500,
                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
  ativo = forms.BooleanField(label = "Ativo", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  padrao = forms.BooleanField(label = "Padão", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  nova_data = forms.BooleanField(label = "Nova data", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  
  class Meta:
    model = Modalidade_Licitacao
    fields = ('nome', 'ativo', 'padrao', 'nova_data')
