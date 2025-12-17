from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Categoria
from .serializers import CategoriaSerializer

from drf_spectacular.utils import extend_schema
@extend_schema(
    tags=["Categorias"],
    summary="Lista e cria categorias",
    description="Endpoint para listagem e criação de categorias."
)

# Create your views here.
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_permissions(self): 
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
    

    class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Categoria.objects.all()
        serializer_class = CategoriaSerializer
        permission_classes = [IsAuthenticated]