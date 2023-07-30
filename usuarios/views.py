from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario
from django.urls import reverse_lazy

from django.views.generic import ListView
from .forms import UsuarioForm


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'  # Crea este template más adelante
    fields = ['nombre', 'correo_electronico', 'password', 'tipo', 'status']

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'  # Crea este template más adelante
    fields = ['nombre', 'correo_electronico', 'password', 'tipo', 'status']

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'  # Crea este template más adelante
    success_url = reverse_lazy('usuarios-list')  # Reemplaza 'usuarios-list' con el nombre de la URL de lista de usuarios


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página principal después de guardar el usuario
    else:
        form = UsuarioForm()

    return render(request, 'usuario_form.html', {'form': form})


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'  # Reemplaza 'usuario_list.html' con el nombre de tu plantilla para mostrar la lista de usuarios

class UsuarioListarView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'  # Reemplaza 'usuario_list.html' con el nombre de tu plantilla para mostrar la lista de usuarios
