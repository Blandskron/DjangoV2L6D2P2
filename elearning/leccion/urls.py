from django.urls import path
from . import views

urlpatterns = [
    path('', views.lecciones_list, name='lecciones_list'),
    path('crear/', views.crear_leccion, name='crear_leccion'),
    path('<int:id>/', views.detalle_leccion, name='detalle_leccion'),
    path('<int:id>/editar/', views.editar_leccion, name='editar_leccion'),
    path('<int:id>/eliminar/', views.eliminar_leccion, name='eliminar_leccion'),
]