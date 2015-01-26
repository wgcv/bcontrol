#encoding:utf-8
from django import forms
from django.forms import ModelForm
from personal.models import Bombero
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime

class BomberoForm(ModelForm):
	fechaIngreso = forms.DateField(widget=SelectDateWidget(years = range( datetime.date.today().year+1,datetime.date.today().year-30)))
	fechaIngreso.label = 'Fecha ingreso institución'
	fechaIngresoCompania = forms.DateField(widget=SelectDateWidget(years = range( datetime.date.today().year+1,datetime.date.today().year-30)))
	fechaIngresoCompania.label = 'Fecha ingreso compañía'
	class Meta:
		model = Bombero
		exclude = ('usuario',)
		

class UsuarioForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')


###    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
