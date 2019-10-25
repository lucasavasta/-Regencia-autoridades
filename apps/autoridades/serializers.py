# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (
	Turno, Profesor, Asignatura, Seguimiento
)

class TurnoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Turno
		fields = ['turnos']


class ProfesorSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Profesor
		fields = ['dni', 'nombre', 'apellido']


class AsignaturaSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Asignatura
		fields = ['codigo', 'nombre', 'año']


class SeguimientoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Seguimiento
		fields = ['fecha', 'profesor', 'turno', 'curso', 'division', 'asignatura', 'ausente', 'tarde']

