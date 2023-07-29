# En forms.py

from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo_electronico', 'password', 'tipo', 'status']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.id = None  # Esto permitirá que la base de datos genere automáticamente el valor para el campo 'id'
        if commit:
            instance.save()
        return instance

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo_electronico', 'password', 'tipo', 'status']
