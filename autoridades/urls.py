from django.urls import include, path
from rest_framework import routers
from .views import (
	TurnoViewsSet,
	ProfesorViewsSet,
	AsignaturaViewsSet,
	SeguimientoViewsSet,
)


router = routers.DefaultRouter()
router.register('turno', TurnoViewsSet)
router.register('profesor', ProfesorViewsSet)
router.register('asignuta', AsignaturaViewsSet)
router.register('seguimiento', SeguimientoViewsSet)


urlpatterns = [
	path('', include(router.urls))
]
