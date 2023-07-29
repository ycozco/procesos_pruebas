# En urls.py de tu aplicación de usuarios

from django.urls import path
from . import views
from .views import UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView

app_name = 'nombre_app'  # Reemplaza 'nombre_app' por el nombre de tu aplicación

urlpatterns = [
    path('', UsuarioListView.as_view(), name='index'),
    path('crear/', UsuarioCreateView.as_view(), name='usuarios_create'),
    path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuarios_update'),
    path('eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuarios_delete'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
]

