from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'juego', juegoViewSet, basename='jueguito')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/juegos/<int:pk>/editar/', views.editar_juego, name='editar_juego'),
    path('api/juegos/<int:pk>/eliminar/', views.eliminar_juego, name='eliminar_juego'),
]

