from django import forms
from .models import juego

class juegoformulario(forms.ModelForm):
    class Meta:
        model = juego
        fields = ['nombre', 'consola', 'precio', 'imagen', 'cantidad', 'estado']
