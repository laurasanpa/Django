# mi_aplicacion/urls.py

from django.urls import path
from . import views
from .views import Home
from django.conf.urls import include, url


urlpatterns = [
  path('libros', views.mostrar_libros, name='mostrar_libros'),
  path('crear_libro', views.crear_libro, name='crear_libro'),
  path('crear_prestamo', views.crear_prestamo, name='crear_prestamo'),
  path('prestamos', views.mostrar_prestamos, name='mostrar_prestamos'),
  path('prestamos/borrar', views.borrar_prestamo, name='borrar_prestamo'),
  path('libros/borrar', views.borrar_libro, name='borrar_libro'),
  path('prestamos/editar', views.editar_prestamo, name='editar_prestamo'),
  path('libros/editar', views.editar_libro, name='editar_libro'),
  path('', Home.as_view(), name='index'),
  path('accounts/', include('django.contrib.auth.urls')),
]