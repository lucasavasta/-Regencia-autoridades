from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
	TurnoSerializer,
	ProfesorSerializer,
	AsignaturaSerializer,
	SeguimientoSerializer,
)
from .models import (
	Turno,
	Profesor,
	Asignatura,
	Seguimiento,
)

class TurnoViewsSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer

class ProfesorViewsSet(viewsets.ModelViewSet):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer

class AsignaturaViewsSet(viewsets.ModelViewSet):
	queryset = Asignatura.objects.all()
	serializer_class = AsignaturaSerializer

class SeguimientoViewsSet(viewsets.ModelViewSet):
	queryset = Seguimiento.objects.all()
	serializer_class = SeguimientoSerializer


