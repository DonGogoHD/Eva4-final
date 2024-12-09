from django.shortcuts import render

# Create your views here.
# views.py
from EvaApp.models import juego
from rest_framework import viewsets
from .serializers import juegosSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class juegoViewSet(viewsets.ModelViewSet):
    queryset = juego.objects.all()
    serializer_class = juegosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['PUT'])
def editar_juego(request, pk):
    try:
        juego_instance = juego.objects.get(pk=pk)
    except juego.DoesNotExist:
        return Response({'detail': 'Juego no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = juegosSerializer(juego_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_juego(request, pk):
    try:
        juego_instance = juego.objects.get(pk=pk)
    except juego.DoesNotExist:
        return Response({'detail': 'Juego no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        juego_instance.delete()
        return Response({'detail': 'Juego eliminado'}, status=status.HTTP_204_NO_CONTENT)