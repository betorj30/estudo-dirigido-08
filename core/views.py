from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from .models import Unidades, Salas, Status, Bem, Categoria
from .serializers import (
    UnidadeSerializer,
    SalaSerializer,
    StatusSerializer,
    BemSerializer,
    CategoriaSerializer,
)
def home(request):
    return HttpResponse("Bem-vindo ao sistema de inventário de bens!")

class UnidadeListCreate(generics.ListCreateAPIView):
    queryset = Unidades.objects.all()
    serializer_class = UnidadeSerializer


class SalaListCreate(generics.ListCreateAPIView):
    queryset = Salas.objects.all()
    serializer_class = SalaSerializer


class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class BemListCreate(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer


class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer