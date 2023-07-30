from django.urls import path
from .views import UsuarioListView, UsuarioCreateView, UsuarioListarView

app_name = 'usuarios'  # Reemplaza 'nombre_app' por el nombre de tu aplicación

urlpatterns = [
    path('', UsuarioListView.as_view(), name='index'),
    path('crear/', UsuarioCreateView.as_view(), name='usuarios-create'),
    path('listar/', UsuarioListarView.as_view(), name='usuarios-listar'),  # Nueva ruta para listar usuarios
    #path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuarios-update'),
    #path('eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuarios-delete'),
]
