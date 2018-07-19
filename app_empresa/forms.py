from django import forms
from .models import *

class FormEmpresa(forms.ModelForm):
	cnpj = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={"class":"form-control"}))
	fantasia = forms.CharField(max_length=300, required= False,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	atividade_principal = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	atividades_secundarias =	forms.CharField(max_length=1500000, widget=forms.Textarea(attrs={"class":"form-control",'readonly':'readonly'}))
	capital_social = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	data_situacao = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	uf = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	natureza_juridica = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	abertura = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	situacao = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	email = forms.CharField(max_length=150, initial = "@",widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	telefone = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	bairro = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	cidade = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
	class Meta:
		model = Empresa
		fields = "__all__"