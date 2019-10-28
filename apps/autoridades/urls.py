from django.urls import include, path
from rest_framework import routers
from .views import (
	ProfesorViewsSet,
	AsignaturaViewsSet,
	IndexView,
	SeguimientoDetail,
	SeguimientoUpdate,
	SeguimientoCreate,
	SeguimientoDelete,

)

app_name = 'autoridades'

router = routers.DefaultRouter()
router.register('asignatura', AsignaturaViewsSet)
router.register('profesor', ProfesorViewsSet)


urlpatterns = [
	path('', include(router.urls)),
	path('principal', IndexView.as_view(), name='index'),
    path('seguimiento/detalle/<int:pk>', SeguimientoDetail.as_view(), name='detalle'),
    path('seguimiento/crear/', SeguimientoCreate.as_view(), name='crear'),
    path('seguimiento/actualizar/<int:pk>', SeguimientoUpdate.as_view(), name='actualizar'),
    path('seguimiento/eliminar/<int:pk>', SeguimientoDelete.as_view(), name='eliminar'),


]

