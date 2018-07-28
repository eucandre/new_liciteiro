# coding=utf-8
from django import forms
from .models import *

class FormEstado(forms.ModelForm):
  nome = forms.CharField(max_length = 150, widget = forms.TextInput(attrs = {"class": "form-control"}))
  acronimo = forms.CharField(label = 'Acrônimo', max_length = 10,
                    widget = forms.TextInput(attrs = {'class': 'form-control'}))
  codigo = forms.CharField(label = 'Código', max_length = 3,
                             widget = forms.TextInput(attrs = {'class': 'form-control'}))
  ativo = forms.BooleanField(label = "Ativo", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  
  class Meta:
    model = Estado
    fields = ('nome','acronimo','codigo','ativo')

class FormCidade(forms.ModelForm):
  nome = forms.CharField(max_length = 150, widget = forms.TextInput(attrs = {"class": "form-control"}))
  estado = forms.CharField(label = 'Estado', max_length = 10,
                             widget = forms.TextInput(attrs = {'class': 'form-control'}))
  codigo = forms.CharField(label = 'Código', max_length = 5,
                           widget = forms.TextInput(attrs = {'class': 'form-control'}))
  ativo = forms.BooleanField(label = "Ativo", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  class Meta:
    model = Cidade
    fields = ('nome','estado','codigo','ativo')