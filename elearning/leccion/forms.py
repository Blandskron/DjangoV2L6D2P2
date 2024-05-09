from django import forms
from .models import Leccion

class LeccionForm(forms.ModelForm):
    class Meta:
        model = Leccion
        fields = ['titulo', 'descripcion', 'fecha_publicacion', 'duracion_minutos', 'archivo']
