# serializers.py
from rest_framework import serializers 
from EvaApp.models import *

class juegosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = juego
        fields = ['id','nombre', 'consola', 'precio', 'imagen', 'cantidad', 'estado']
