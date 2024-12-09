from django.shortcuts import render, redirect
from django.contrib.auth import logout
from EvaApp.forms import juegoformulario
from EvaApp.models import juego  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import admin_required
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada ¡Ahora puedes iniciar sesion!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def index(request):
    juegos = juego.objects.all()
    return render(request, 'index.html', {'juegos': juegos})

@login_required
@admin_required
def listajuegos(request):
    juegos = juego.objects.all()
    data = {'juegos': juegos}
    return render(request, 'juegos.html', data)

@login_required
@admin_required
def agregarjuego(request):
    if request.method == 'POST':
        form = juegoformulario(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego agregado')
            return redirect('juegos')  
    else:
        form = juegoformulario()  
    data = {'form': form}
    return render(request, 'agregarjuego.html', data)

@login_required
@admin_required
def eliminarjuego(request, id):
    borrar_juego = juego.objects.get(id=id)
    borrar_juego.delete()
    messages.success(request, 'Juego eliminado') 
    return redirect('juegos')

@login_required
@admin_required
def actualizarjuego(request, id):
    actuali_juego = juego.objects.get(id=id)
    form = juegoformulario(instance=actuali_juego)
    if request.method == 'POST':
        form = juegoformulario(request.POST, instance=actuali_juego)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego actualizado')
            return redirect('juegos')
    data = {'form': form}
    return render(request, 'agregarjuego.html', data)
