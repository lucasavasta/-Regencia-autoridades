from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Profesor(models.Model):
	dni = models.PositiveSmallIntegerField(
		primary_key=True,
		validators=[
			MaxValueValidator(9999),
			MinValueValidator(1)
		]
	)
	nombre = models.CharField(max_length=40, help_text='Ingrese el nombre del profesor.')
	apellido = models.CharField(max_length=40, help_text='Ingrese el apellido del profesor.')

	class Meta:
		verbose_name='Profesor'
		verbose_name_plural = "Profesores"

	def __str__(self):
		return '%s' % (self.nombre)
# Create your models here.
class Asignatura(models.Model):
	codigo = models.PositiveIntegerField('Código asignatura', 
		unique=True,
		validators=[
			MaxValueValidator(999999),
			MinValueValidator(1)
		],
		help_text='Ingrese código de la asignatura.'
	)
	nombre = models.CharField('Nombre de la asignatura', max_length=40, help_text='Ingrese el nombre de la asignatura.')
	año = models.PositiveIntegerField('Año de la asignatura',
		validators=[
			MaxValueValidator(6),
			MinValueValidator(1)
		],
		help_text='Ingrese el año en el que se cursa la asignatura.'
	)

	def __str__(self):
		return '%s %s' % (self.nombre, self.año)

	class Meta:
		verbose_name_plural = 'asignaturas'