"""
URL configuration for procesos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# En procesos/urls.py de tu proyecto
from django.contrib import admin
from django.urls import path, include
from usuarios.views import UsuarioListView, UsuarioCreateView

urlpatterns = [
    path('', UsuarioListView.as_view(), name='index'),  # Ruta raíz que muestra la lista de usuarios
    path('admin/', admin.site.urls),  # Ruta para el sitio de administración de Django
    path('usuarios/', include('usuarios.urls')),  # Ruta para la aplicación de usuarios
]
