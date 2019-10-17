from django.contrib import admin
from .models import (
	Profesor, Asignatura
)
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
	list_filter = ('dni', 'nombre')

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
	list_filter = ['codigo']