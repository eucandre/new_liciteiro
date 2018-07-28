from django import forms
from .models import *

class FormCnaesDivisoes(forms.ModelForm):
  class Meta:
    model = Cnaes_divisoes
    fields = '__all__'

class FormCnaesSessoes(forms.ModelForm):
  class Meta:
    model = Cnaes_sessoes
    fields = '__all__'

class FormCnaesGrupos(forms.ModelForm):
  class Meta:
    model = Cnaes_grupos
    fields = '__all__'

class FormCnaesClasses(forms.ModelForm):
  class Meta:
    model = Cnaes_classes
    fields = '__all__'

class FormCnaesSubClasses(forms.ModelForm):
  class Meta:
    model = Cnaes_sub_classes
    fields = '__all__'