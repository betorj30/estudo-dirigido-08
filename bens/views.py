from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Bem
from .serializers import BemSerializer

from drf_spectacular.utils import extend_schema
@extend_schema(
    tags=["Bens"],
    summary="Lista e cria bens",
    description="Endpoint para listagem e criação de bens patrimoniais."
)

# Create your views here.

class BemListCreateView(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
    

class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
    permission_classes = [IsAuthenticated]    
    
