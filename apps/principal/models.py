from django.db import models

class Alumno(models.Model):
	nombre = models.CharField(max_length=200)
	pais   = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre
		

class Nota(models.Model):
	alumno = models.ForeignKey('Alumno')
	materia = models.CharField(max_length=50)
	calificacion = models.IntegerField()

	def __unicode__(self):
		return self.alumno.nombre
 