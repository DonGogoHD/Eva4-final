from django.db import models
from django.contrib.auth.models import User
from EvaApp.models import juego  

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username} ({self.id})"

class ProductoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='productos', on_delete=models.CASCADE)
    juego = models.ForeignKey(juego, on_delete=models.CASCADE) 
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.juego.nombre} en carrito"