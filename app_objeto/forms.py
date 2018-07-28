from django import forms
from app_objeto.models import *

class FormObjeto(forms.ModelForm):
  nome = forms.CharField(label = 'Objeto', max_length = 500, widget = forms.TextInput(attrs = {'class':'form-control'}))
  ativo = forms.BooleanField(widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  sessoes_cnaes = forms.ModelMultipleChoiceField(label = 'Atividades',queryset = Cnaes_sessoes.objects.all(), widget = forms.CheckboxSelectMultiple())
  
  
  class Meta:
    model = Objeto
    fields = ('nome', 'ativo', 'sessoes_cnaes')