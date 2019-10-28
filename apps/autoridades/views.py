from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .serializers import (
	ProfesorSerializer,
	AsignaturaSerializer,
	SeguimientoSerializer,
)
from .models import (
	Profesor,
	Asignatura,
	Seguimiento,
)

class IndexView(LoginRequiredMixin, ListView):
	model = Seguimiento
	template_name = 'index.html'
	context_object_name = 'seguimientos'

class ProfesorViewsSet(viewsets.ModelViewSet):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer

class AsignaturaViewsSet(viewsets.ModelViewSet):
	queryset = Asignatura.objects.all()
	serializer_class = AsignaturaSerializer

class SeguimientoDetail(LoginRequiredMixin, DetailView):
	model = Seguimiento
	template_name = 'detalle.html'
	context_object_name = 'segui'

class SeguimientoCreate(LoginRequiredMixin, CreateView):
	model = Seguimiento
	fields = ['profesor', 'turno', 'curso', 'division', 'asignatura', 'ausente', 'tarde']
	template_name = 'crear.html'
	success_url = reverse_lazy('autoridades:index')

class SeguimientoUpdate(LoginRequiredMixin, UpdateView):
	model = Seguimiento
	fields = ['profesor', 'turno', 'curso', 'division', 'asignatura', 'ausente', 'tarde']
	template_name = 'actualizar.html'
	success_url = reverse_lazy('autoridades:index')

class SeguimientoDelete(LoginRequiredMixin, DeleteView):
	model = Seguimiento
	template_name = 'eliminar.html'
	success_url = reverse_lazy('autoridades:index')
