# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (
	Profesor, Asignatura
)


class ProfesorSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Profesor
		fields = ['dni', 'nombre', 'apellido']


class AsignaturaSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Asignatura
		fields = ['codigo', 'nombre', 'año']