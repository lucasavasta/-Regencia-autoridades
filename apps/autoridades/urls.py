from django.urls import include, path
from rest_framework import routers
from .views import (
	TurnoViewsSet,
	ProfesorViewsSet,
	AsignaturaViewsSet,
	SeguimientoCreate,
)

app_name = 'autoridades'

router = routers.DefaultRouter()
router.register('turno', TurnoViewsSet)
router.register('asignatura', AsignaturaViewsSet)
router.register('profesor', ProfesorViewsSet)


urlpatterns = [
	path('', include(router.urls)),
    path('seguimiento/create/', SeguimientoCreate.as_view(), name='seguimiento'),
]

