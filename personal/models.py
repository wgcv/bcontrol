#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from compania.models import Compania
from curso.models import Curso
# Create your models here.


class Rango(models.Model):
	rango = models.CharField(max_length = 50, null = False)
	planaMayor = models.BooleanField(default = False)
	def __unicode__(self):
		return self.rango

class Bombero(models.Model):
	nombre = models.CharField(max_length = 50, null = False, blank = False, verbose_name ='Primer nombre')
	nombreSegundo = models.CharField(max_length = 50, null = True, blank = True, verbose_name ='Segundo nombre')
	apellido = models.CharField(max_length = 50, null = False, blank = False, verbose_name ='Primer apellido')
	apellidoSegundo = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'Segundo Apellido')
	cedulaIdentidad = models.CharField(max_length = 10, null = False, blank = False, unique = True, verbose_name ='Cédula de identidad')
	cedulaBomberil = models.IntegerField(max_length = 5, null = False, blank = False, unique = True, verbose_name ='Cédula Bomberil',help_text='Cédula Bomberil 5 dítgitos')
	fechaIngreso = models.DateField(verbose_name ='Fecha ingreso institución', help_text='Formato: DD/MM/AAAA')
	fechaIngresoCompania = models.DateField(verbose_name ='Fecha ingreso compañía', help_text='Formato: DD/MM/AAAA')
	correo = models.EmailField (max_length=75, verbose_name ='Correo electrónico')
	celular = models.CharField(max_length = 10, blank = True, unique = False, verbose_name ='Número de celular')
	epp = models.BooleanField(default = False, verbose_name ='Posée equipo de combate')
	activo = models.BooleanField(default = True, verbose_name ='Activo en la institución')
	compania = models.ForeignKey(Compania, verbose_name ='Compañía que pertenece')
	rango = models.ForeignKey(Rango, verbose_name ='Rango')
	tipoSangre = models.CharField(max_length = 3, verbose_name ='Tipo de sangre (RH)', choices = (
		('O+','O+'),
		('O-','O-'),
		('A+','A+'),
		('A-','A-'),
		('B+','B+'),
		('B-','B-'),
		('AB+','AB+'),
		('AB-','AB-'),))
	cursos = models.ManyToManyField(Curso, blank=True, verbose_name ='Cursos realizados')
	usuario = models.ForeignKey(User)



	def __unicode__(self):
		return '%s || %s %s' % (self.cedulaBomberil, self.nombre, self.apellido)




