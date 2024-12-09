from django import forms
from .models import ProductoCarrito
from EvaApp.models import juego 

class AgregarAlCarritoForm(forms.ModelForm):
    class Meta:
        model = ProductoCarrito
        fields = ['juego', 'cantidad']

    juego = forms.ModelChoiceField(
        queryset=juego.objects.all(), 
        empty_label="Seleccione un juego"
    )
    cantidad = forms.IntegerField(min_value=1, initial=1, label='Cantidad')
