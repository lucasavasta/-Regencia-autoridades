from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
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


class SeguimientoCreate(CreateView):
	model = Seguimiento
	fields = ['profesor', 'turno', 'curso', 'division', 'asignatura', 'ausente', 'tarde']
	template_name = 'formulario.html'
	success_url = reverse_lazy('autoridades:seguimiento')



