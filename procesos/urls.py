from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuarioListView, UsuarioCreateView

urlpatterns = [
    path('', UsuarioListView.as_view(), name='index'),  # Ruta raíz que muestra la lista de usuarios
    path('admin/', admin.site.urls),  # Ruta para el sitio de administración de Django
    path('usuarios/', include('usuarios.urls')),  # Ruta para la aplicación de usuarios
]
