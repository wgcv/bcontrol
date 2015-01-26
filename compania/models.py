from django.db import models

# Create your models here.

class Brigada(models.Model):
	nombre = models.CharField(max_length = 100, null = False)
	numero = models.IntegerField(max_length = 2, null = False, blank = False, unique = True)
	def __unicode__(self):
		return '%s - %s' % (self.numero, self.nombre)

class Compania(models.Model):
	nombre = models.CharField(max_length = 100, null = False)
	numero = models.IntegerField(max_length = 2, null = False, blank = False, unique = True)
	brigada = models.ForeignKey(Brigada)

	def __unicode__(self):
		return '%s - %s' % (self.numero, self.nombre)
