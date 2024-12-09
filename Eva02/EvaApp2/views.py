from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, ProductoCarrito
from .forms import AgregarAlCarritoForm
from EvaApp.models import juego
from django.http import Http404

@login_required
def lista_juegos(request):
    juegos = juego.objects.all()

    nombre = request.GET.get('nombre', '')
    consola = request.GET.get('consola', '')
    ordenar_precio = request.GET.get('ordenar_precio', '')

    if nombre:
        juegos = juegos.filter(nombre__icontains=nombre)
    
    if consola:
        juegos = juegos.filter(consola=consola)

    if ordenar_precio == 'asc':
        juegos = juegos.order_by('precio')
    elif ordenar_precio == 'desc':
        juegos = juegos.order_by('-precio')

    return render(request, 'EvaApp2/buscarjuegos.html', {'juegos': juegos})


@login_required
def agregar_al_carrito(request, juego_id):
    try:
        juego_obj = juego.objects.get(id=juego_id) 
    except juego.DoesNotExist:
        raise Http404("Juego no encontrado") 

    usuario = request.user
    carrito, _ = Carrito.objects.get_or_create(usuario=usuario) 

    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            producto_existente = ProductoCarrito.objects.filter(carrito=carrito, juego=juego_obj).first()
            if producto_existente:
                producto_existente.cantidad += cantidad
                producto_existente.save() 
            else:
                ProductoCarrito.objects.create(carrito=carrito, juego=juego_obj, cantidad=cantidad)  
            return redirect('ver_carrito')  
    else:
        form = AgregarAlCarritoForm(initial={'juego': juego_obj})

    return render(request, 'EvaApp2/ver_carrito', {'form': form, 'juego': juego_obj})


@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    productos = carrito.productos.all()  
    total = sum([producto.juego.precio * producto.cantidad for producto in productos])  
    return render(request, 'EvaApp2/ver_carrito.html', {'productos': productos, 'total': total})

@login_required
def eliminar_producto(request, producto_id):
    producto = ProductoCarrito.objects.get(id=producto_id)
    if producto.carrito.usuario == request.user:
        producto.delete()
    return redirect('ver_carrito')
