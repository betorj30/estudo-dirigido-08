from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Salas
from .serializers import SalaSerializer
from drf_spectacular.utils import extend_schema
@extend_schema(
    tags=["Salas"],
    summary="Lista e cria salas",
    description="Endpoint para listagem e criação de salas."
)
# Create your views here.
class SalaListCreate(generics.ListCreateAPIView):
    queryset = Salas.objects.all()
    serializer_class = SalaSerializer

    def get_permissions(self): 
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
    

    class SalaDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Salas.objects.all()
        serializer_class = SalaSerializer
        permission_classes = [IsAuthenticated]