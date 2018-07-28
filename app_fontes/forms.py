from django import forms
from .models import *

UF = ((u'AC','AC'),(u'AL','AL'),(u'AP','AP'),(u'AM','AM'),(u'BA','BA'),(u'CE','CE'),(u'DF','DF'),(u'ES','ES'),
			(u'GO','GO'),(u'MA','MA'),(u'MT','MT'),(u'MS','MS'),(u'MG','MG'),(u'PA','PA'),(u'PB','PB'),
			(u'PR', 'PR'),(u'PE','PE'),(u'PI','PI'),(u'RJ','RJ'),(u'RN','RN'),(u'RS','RS'),(u'RO','RO'),(u'RR','RR'),
			(u'SC','SC'),(u'SP','SP'),(u'SE','SE'),(u'TO','TO'))


class FormFonte(forms.ModelForm):
  nome = forms.CharField(label = 'Nome da Categoria', max_length = 500,
                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
  uf = forms.ChoiceField(choices = UF, widget = forms.Select(attrs = {'class':'form-control'}))
  ativo = forms.BooleanField(label = "Ativo", widget = forms.CheckboxInput(attrs = {'class': 'form-control'}))
  class Meta:
    model = Fonte
    fields = ('nome', 'uf', 'ativo')