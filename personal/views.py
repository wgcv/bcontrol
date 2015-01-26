from django.shortcuts import render
from datetime import datetime
from personal.forms import *
from django.contrib.auth.models import User
from personal.models import Bombero

# Create your views here.

def home(request):
	now = datetime.date.today()
	return render(request,'index.html', {'hora' : now})

def agregarBombero(request):
	if request.method == "POST":
		formBombero = BomberoForm(request.POST)
		formUsuario = UsuarioForm(request.POST)
		if (formBombero.is_valid() and formUsuario.is_valid()):
			usuario = formUsuario.save(commit = False)
			bombero = formBombero.save(commit = False)
			usuario.email = bombero.correo
			usuario.first_name = bombero.nombre
			usuario.last_name = bombero.apellido
			usuario.save()
			bombero.usuario = usuario
			bombero.save()
			return  render(request,'index.html', {'hora' : 'Agregado con exito'})
	else:
		formBombero = BomberoForm
		formUsuario = UsuarioForm
	return render(request,'agregarBombero.html',{'formBombero': formBombero, 'formUsuario':formUsuario})

def agregarUsuario(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			now = 'agregado'
			return  render(request,'index.html', {'hora' : now})
	else:
			form = UsuarioForm
	return render(request,'agregarBombero.html',{'form': form})


def perfil(request,d):
	bombero = Bombero.objects.get(usuario = User.objects.get(username=d))
	return  render(request,'perfil.html', {'perfil' : bombero})
