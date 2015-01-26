from django.db import models

# Create your models here.
class Curso(models.Model):
	nombre = models.CharField(max_length = 225, null = False)
	horas = models.IntegerField(max_length = 3, null = True, blank = True)

	def __unicode__(self):
		return self.nombre