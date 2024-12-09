from django.contrib import admin
from EvaApp.models import juego

# Register your models here.

class adminjuego(admin.ModelAdmin):
    actions = ['juegos_actualizados']
    ordering = ['nombre']
    search_fields = ['nombre', 'consola']
    list_filter = ['precio', 'estado']
    list_display = ['nombre', 'precio', 'estado']

    def precio_actualizado(self, request, queryset):
        queryset.update(precio = None)
        self.message_user(request,"Se actualizo el precio del juego" )
    precio_actualizado.short_description = "precio actualizado"

admin.site.register(juego, adminjuego)