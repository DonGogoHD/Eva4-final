from django.contrib import admin
from django.urls import path
from AdminAPi.views import juegoViewSet
from EvaApp import views as evaapp_views  
from EvaApp2 import views as carrito_views  
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'juego', juegoViewSet, basename='jueguito')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', evaapp_views.index, name='index'),
    path('juegos/', evaapp_views.listajuegos, name='juegos'),
    path('agregarjuego/', evaapp_views.agregarjuego, name='agregar_juego'),
    path('eliminarjuego/<int:id>', evaapp_views.eliminarjuego, name='eliminar_juego'),
    path('actualizarjuego/<int:id>', evaapp_views.actualizarjuego, name='editar_juego'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registro/', evaapp_views.registro, name='registro'),
    path('cerrar_sesion/', auth_views.LogoutView.as_view(next_page='index'), name='logout'), 
    path('ver_carrito/', carrito_views.ver_carrito, name='ver_carrito'), 
    path('buscarjuegos/', carrito_views.lista_juegos, name='buscarjuegos'),
    path('agregar_al_carrito/<int:juego_id>/', carrito_views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_producto/<int:producto_id>/', carrito_views.eliminar_producto, name='eliminar_producto'),
    path('api/', include('AdminAPi.urls')),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
