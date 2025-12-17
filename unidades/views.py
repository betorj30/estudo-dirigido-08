from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Unidades
from .serializers import UnidadeSerializer
from drf_spectacular.utils import extend_schema
@extend_schema(
    tags=["Unidades"],
    summary="Lista e cria unidades",
    description="Endpoint para listagem e criação de unidades."
)

# Create your views here.
class UnidadeListCreate(generics.ListCreateAPIView):
    queryset = Unidades.objects.all()
    serializer_class = UnidadeSerializer

    def get_permissions(self): 
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
    

    class UnidadeDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Unidades.objects.all()
        serializer_class = UnidadeSerializer
        permission_classes = [IsAuthenticated]