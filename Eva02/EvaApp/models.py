from django.db import models

class juego(models.Model):
    nombre = models.CharField(max_length=100)
    consola = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre